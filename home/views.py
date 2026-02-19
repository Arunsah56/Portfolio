from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, Skill, Contact  # Make sure these models exist

def home(request):
    # Try to get projects, but handle if table doesn't exist yet
    try:
        projects = Project.objects.all()[:3]
    except:
        projects = []
    
    try:
        skills = Skill.objects.all()
    except:
        skills = []
    
    context = {
        'projects': projects,
        'skills': skills,
    }
    return render(request, 'home.html', context)  # Changed path

def projects(request):
    try:
        projects = Project.objects.all().order_by('-date_created')
    except:
        projects = []
    return render(request, 'projects.html', {'projects': projects})

from django.core.mail import send_mail   # ⭐ ADDED IMPORT
from django.conf import settings   

# def contact(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')
#         if not name or not email or not message:
#             messages.error(request, 'Please fill all required fields.')
#             return redirect('contact')
#         try:
#             Contact.objects.create(
#                 name=name,
#                 email=email,
#                 message=message
#             )
#             send_mail(
#                 subject=f'New Contact Message from {name}',
#                 message=f"You received a new contact message: Name: {name} Email: {email} Message: {message}",
#                 from_email=settings.EMAIL_HOST_USER,
#                 recipient_list=[settings.EMAIL_HOST_USER],  # sends to YOU
#             )
#             messages.success(request, 'Your message has been sent successfully!')
#         except:
#             messages.error(request, 'There was an error sending your message.')
        
#         return redirect('contact')
    
#     return render(request, 'contact.html')

from .forms import ContactForm   # 🟢 NEW IMPORT
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact
# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)   # 🟢 NEW

#         if form.is_valid():   # 🟢 NEW VALIDATION
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             subject = form.cleaned_data['subject']
#             message = form.cleaned_data['message']
#             # contact = form.save() 

#             try:
#                 Contact.objects.create(
#                     name=name,
#                     email=email,
#                     subject=subject,
#                     message=message
#                 )

#                 send_mail(
#                     subject=f'New Contact Message from {name}',
#                     message=f""" Hi {name}, Thank you for contacting me. Your message has been received. I will get back to you soon. Message: {message}""",
#                     from_email=settings.EMAIL_HOST_USER,
#                     recipient_list=[settings.EMAIL_HOST_USER],
#                 )

#                 messages.success(request, 'Your message has been sent successfully!')
#                 return redirect('contact')

#             except Exception as e:
#                 messages.error(request, 'There was an error sending your message.')

#     else:
#         form = ContactForm()   # 🟢 NEW

#     return render(request, 'contact.html', {'form': form})   # 🟢 MODIFIED

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data["email"]
            name = form.cleaned_data["name"]
            message = form.cleaned_data["message"]
            # Save the contact message to the database

            Contact.objects.create(
                name=name,
                email=user_email, 
                message=message
                )
            # Send auto greeting email
            send_mail(
                subject="Thanks for contacting us!",
                message=f"Hi {name},\n\nThank you for reaching out. We will get back to you soon 😊",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user_email],
            )

            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')

    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})

def about(request):
    try:
        skills = Skill.objects.all()
    except:
        skills = []
    return render(request, 'about.html', {'skills': skills})