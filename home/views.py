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

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        try:
            Contact.objects.create(
                name=name,
                email=email,
                message=message
            )
            send_mail(
                subject=f'New Contact Message from {name}',
                message=f"You received a new contact message: Name: {name} Email: {email} Message: {message}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],  # sends to YOU
            )
            messages.success(request, 'Your message has been sent successfully!')
        except:
            messages.error(request, 'There was an error sending your message.')
        
        return redirect('contact')
    
    return render(request, 'contact.html')

def about(request):
    try:
        skills = Skill.objects.all()
    except:
        skills = []
    return render(request, 'about.html', {'skills': skills})