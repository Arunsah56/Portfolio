from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
import logging

from .models import Project, Experience, ContactMessage, Blog, Education
from .forms import ContactForm

logger = logging.getLogger(__name__)


def _handle_contact_form(request):
    """Validate, save to DB, and send email. Returns (success: bool, form)."""
    form = ContactForm(request.POST)
    if form.is_valid():
        contact = form.save()

        # Send email notification to admin
        subject = f'New Contact Message from {contact.name}'
        html_body = f"""
        <html>
            <body>
                <h2>New Contact Message</h2>
                <p><strong>Name:</strong> {contact.name}</p>
                <p><strong>Email:</strong> {contact.email}</p>
                <p><strong>Message:</strong></p>
                <p>{contact.message.replace(chr(10), '<br>')}</p>
            </body>
        </html>
        """
        
        try:
            send_mail(
                subject,
                f"Name: {contact.name}\nEmail: {contact.email}\nMessage:\n{contact.message}",
                settings.DEFAULT_FROM_EMAIL,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
                html_message=html_body,
            )
            logger.info(f'✓ Admin notification email sent for message from {contact.email}')
        except Exception as e:
            # Email sending failed but the message is already saved in DB
            logger.error(f'✗ Failed to send admin email: {type(e).__name__}: {str(e)}')
            messages.warning(request, f'Message saved but admin notification failed: {str(e)}')

        # Send confirmation email to the visitor
        try:
            html_content = render_to_string(
                'main/emails/confirmations_email.html',
                {'name': contact.name, 'message': contact.message},
            )
            send_mail(
                'Thank You for Reaching Out — Arun Sah\'s Portfolio',
                f'Hi {contact.name}, thank you for visiting my portfolio and reaching out. I have received your message and will get back to you soon.',
                settings.DEFAULT_FROM_EMAIL,
                [contact.email],
                fail_silently=False,
                html_message=html_content,
            )
            logger.info(f'✓ Confirmation email sent to {contact.email}')
        except Exception as e:
            # Confirmation email failed but the message is already saved
            logger.error(f'✗ Failed to send confirmation email to {contact.email}: {type(e).__name__}: {str(e)}')
            messages.warning(request, f'Your message was saved but confirmation email failed: {str(e)}')

        return True, form
    return False, form


def home(request):
    if request.method == 'POST':
        success, form = _handle_contact_form(request)
        if success:
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()

    context = {
        'form': form,
        'educations': Education.objects.all(),
        'experiences': Experience.objects.all(),
        'projects': Project.objects.all(),
        'blogs': Blog.objects.filter(is_published=True),
    }
    return render(request, 'main/home.html', context)


def about(request):
    experiences = Experience.objects.all()
    return render(request, 'main/about.html', {'experiences': experiences})


def projects(request):
    projects = Project.objects.all()
    return render(request, 'main/projects.html', {'projects': projects})


def contact(request):
    if request.method == 'POST':
        success, form = _handle_contact_form(request)
        if success:
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()

    return render(request, 'main/contact.html', {'form': form})


def blog(request):
    blogs = Blog.objects.filter(is_published=True)
    return render(request, 'main/blog.html', {'blogs': blogs})


# ============================================================
# CUSTOM ADMIN PANEL VIEWS
# ============================================================
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import ContactMessage
from .admin_forms import ProjectForm, BlogForm, EducationForm, ExperienceForm

# Model configuration map for DRY CRUD
MODEL_CONFIG = {
    'project': {
        'model': Project,
        'form': ProjectForm,
        'icon': 'fa-folder-open',
        'label': 'Project',
    },
    'blog': {
        'model': Blog,
        'form': BlogForm,
        'icon': 'fa-pen-to-square',
        'label': 'Blog Post',
    },
    'education': {
        'model': Education,
        'form': EducationForm,
        'icon': 'fa-graduation-cap',
        'label': 'Education',
    },
    'experience': {
        'model': Experience,
        'form': ExperienceForm,
        'icon': 'fa-briefcase',
        'label': 'Experience',
    },
    'contactmessage': {
        'model': ContactMessage,
        'form': None,
        'icon': 'fa-envelope',
        'label': 'Contact Message',
    },
}


def _admin_context():
    """Common context for all admin pages (sidebar counts)."""
    return {
        'project_count': Project.objects.count(),
        'blog_count': Blog.objects.count(),
        'education_count': Education.objects.count(),
        'experience_count': Experience.objects.count(),
        'message_count': ContactMessage.objects.count(),
    }


def admin_login(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('admin_dashboard')

    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            error = 'Invalid credentials or insufficient permissions.'

    return render(request, 'main/admin_login.html', {'error': error})


@login_required(login_url='admin_login')
def admin_logout(request):
    logout(request)
    return redirect('home')


@login_required(login_url='admin_login')
def admin_dashboard(request):
    context = _admin_context()
    context.update({
        'active_tab': 'dashboard',
        'projects': Project.objects.all(),
        'blogs': Blog.objects.all(),
        'educations': Education.objects.all(),
        'experiences': Experience.objects.all(),
        'contact_messages': ContactMessage.objects.all().order_by('-created_at'),
    })
    return render(request, 'main/admin_dashboard.html', context)


@login_required(login_url='admin_login')
def admin_add(request, model_name):
    config = MODEL_CONFIG.get(model_name)
    if not config or not config['form']:
        return redirect('admin_dashboard')

    if request.method == 'POST':
        form = config['form'](request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'{config["label"]} added successfully!')
            return redirect('admin_dashboard')
    else:
        form = config['form']()

    context = _admin_context()
    context.update({
        'form': form,
        'form_title': f'Add {config["label"]}',
        'form_icon': config['icon'],
        'submit_label': f'Add {config["label"]}',
        'active_tab': f'{model_name}s',
    })
    return render(request, 'main/admin_form.html', context)


@login_required(login_url='admin_login')
def admin_edit(request, model_name, pk):
    config = MODEL_CONFIG.get(model_name)
    if not config or not config['form']:
        return redirect('admin_dashboard')

    obj = get_object_or_404(config['model'], pk=pk)

    if request.method == 'POST':
        form = config['form'](request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, f'{config["label"]} updated successfully!')
            return redirect('admin_dashboard')
    else:
        form = config['form'](instance=obj)

    context = _admin_context()
    context.update({
        'form': form,
        'form_title': f'Edit {config["label"]}',
        'form_icon': config['icon'],
        'submit_label': 'Save Changes',
        'active_tab': f'{model_name}s',
    })
    return render(request, 'main/admin_form.html', context)


@login_required(login_url='admin_login')
def admin_delete(request, model_name, pk):
    config = MODEL_CONFIG.get(model_name)
    if not config:
        return redirect('admin_dashboard')

    obj = get_object_or_404(config['model'], pk=pk)

    if request.method == 'POST':
        obj.delete()
        messages.success(request, f'{config["label"]} deleted successfully!')
        return redirect('admin_dashboard')

    context = _admin_context()
    context.update({
        'object_name': config['label'],
        'object_title': str(obj),
        'active_tab': f'{model_name}s',
    })
    return render(request, 'main/admin_delete.html', context)
