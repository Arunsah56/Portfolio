from django import forms
from .models import Project, Blog, Education, Experience


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'tech_stack', 'github_link', 'live_link', 'image', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Project title'}),
            'description': forms.Textarea(attrs={'placeholder': 'Describe what the project does...', 'rows': 5}),
            'tech_stack': forms.TextInput(attrs={'placeholder': 'Python, Django, React (comma-separated)'}),
            'github_link': forms.URLInput(attrs={'placeholder': 'https://github.com/...'}),
            'live_link': forms.URLInput(attrs={'placeholder': 'https://myproject.com'}),
            'order': forms.NumberInput(attrs={'placeholder': '1'}),
        }


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Blog post title'}),
            'content': forms.Textarea(attrs={'placeholder': 'Write your blog post content here...', 'rows': 10}),
        }


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['institution', 'degree', 'duration', 'description', 'order']
        widgets = {
            'institution': forms.TextInput(attrs={'placeholder': 'e.g. Lovely Professional University'}),
            'degree': forms.TextInput(attrs={'placeholder': 'e.g. B.Tech in Computer Science'}),
            'duration': forms.TextInput(attrs={'placeholder': 'e.g. August 2023 - Present'}),
            'description': forms.Textarea(attrs={'placeholder': 'Brief description...', 'rows': 4}),
            'order': forms.NumberInput(attrs={'placeholder': '1'}),
        }


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['organization', 'role', 'duration', 'description', 'partner_label', 'github_link', 'order']
        widgets = {
            'organization': forms.TextInput(attrs={'placeholder': 'e.g. Algotutor'}),
            'role': forms.TextInput(attrs={'placeholder': 'e.g. Winter Training — Python Full Stack'}),
            'duration': forms.TextInput(attrs={'placeholder': 'e.g. January 2026 – February 2026'}),
            'description': forms.Textarea(attrs={'placeholder': 'Describe your role and achievements...', 'rows': 5}),
            'partner_label': forms.TextInput(attrs={'placeholder': 'e.g. LPU Winter PEP Training (optional)'}),
            'github_link': forms.URLInput(attrs={'placeholder': 'https://github.com/... (optional)'}),
            'order': forms.NumberInput(attrs={'placeholder': '1'}),
        }
