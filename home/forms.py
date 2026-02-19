# from django import forms

# class ContactForm(forms.Form):
#     name = forms.CharField( max_length=100, widget=forms.TextInput(attrs={'id': 'name'}))
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'id': 'email'}))
#     subject = forms.CharField( required=False, widget=forms.TextInput(attrs={'id': 'subject'}))
#     message = forms.CharField(widget=forms.Textarea(attrs={'id': 'message'}))

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)