from rest_framework import generics, status
from rest_framework.response import Response
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Project, Experience, Blog, Education
from .serializers import (
    ProjectSerializer,
    ExperienceSerializer,
    BlogSerializer,
    ContactMessageSerializer,
    EducationSerializer,
)


class ProjectListAPI(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ExperienceListAPI(generics.ListAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class BlogListAPI(generics.ListAPIView):
    queryset = Blog.objects.filter(is_published=True)
    serializer_class = BlogSerializer


class EducationListAPI(generics.ListAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class ContactCreateAPI(generics.CreateAPIView):
    serializer_class = ContactMessageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        contact = serializer.save()

        # Send email notification (same logic as views._handle_contact_form)
        subject = f'New Contact Message from {contact.name}'
        body = (
            f"Name: {contact.name}\n"
            f"Email: {contact.email}\n"
            f"Message:\n{contact.message}\n"
        )
        try:
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
        except Exception:
            pass

        # Send confirmation email to the visitor
        try:
            html_content = render_to_string(
                'main/emails/confirmation_email.html',
                {'name': contact.name, 'message': contact.message},
            )
            send_mail(
                'Thank You for Reaching Out — Abhay\'s Portfolio',
                f'Hi {contact.name}, thank you for visiting my portfolio and reaching out. '
                f'I have received your message and will get back to you soon.',
                settings.DEFAULT_FROM_EMAIL,
                [contact.email],
                fail_silently=False,
                html_message=html_content,
            )
        except Exception:
            pass

        return Response(
            {'message': 'Your message has been sent successfully!'},
            status=status.HTTP_201_CREATED,
        )
