from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter your name',
                'required': True,
                'id': 'name',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email',
                'required': True,
                'id': 'email',
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Write your message here...',
                'required': True,
                'id': 'message',
            }),
        }
        labels = {
            'name': 'Your Name',
            'email': 'Your Email',
            'message': 'Message',
        }
