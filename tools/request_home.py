import os
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Portfolio.settings')
import django
django.setup()
from django.test import Client
c = Client()
resp = c.get('/')
print('status_code:', resp.status_code)
print('content-length:', len(resp.content))
print(resp.content.decode('utf-8')[:800])
