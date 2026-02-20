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
                'class': 'form-input',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email',
                'required': True,
                'id': 'email',
                'class': 'form-input',
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Write your message here...',
                'required': True,
                'id': 'message',
                'class': 'form-textarea',
            }),
        }
        labels = {
            'name': 'Your Name',
            'email': 'Your Email',
            'message': 'Message',
        }