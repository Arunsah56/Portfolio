import os
import sys
from pathlib import Path

# Ensure project root is on sys.path so `Portfolio` package is importable
sys.path.append(str(Path(__file__).resolve().parent.parent))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Portfolio.settings')

import django
django.setup()

from home.models import Project, Experience, Education, Blog, ContactMessage

print('Counts:')
print('Projects:', Project.objects.count())
print('Experiences:', Experience.objects.count())
print('Educations:', Education.objects.count())
print('Blogs published:', Blog.objects.filter(is_published=True).count())
print('ContactMessages:', ContactMessage.objects.count())
