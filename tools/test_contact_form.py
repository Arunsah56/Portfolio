import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Portfolio.settings')

import django
django.setup()

from home.models import ContactMessage
from home.views import _handle_contact_form
from django.test import RequestFactory
from django.http import QueryDict

print("=" * 70)
print("TESTING EMAIL SYSTEM - Simulating Contact Form Submission")
print("=" * 70)

# Create a fake request with contact form data
factory = RequestFactory()
post_data = {
    'name': 'Test User',
    'email': 'testuser@example.com',
    'message': 'This is a test message to verify the email system is working!'
}

# Create POST request
request = factory.post('/', data=post_data)
request.POST = QueryDict(mutable=True)
for key, value in post_data.items():
    request.POST[key] = value

print(f"\nTest Contact Form Data:")
print(f"  Name: {post_data['name']}")
print(f"  Email: {post_data['email']}")
print(f"  Message: {post_data['message']}")

print(f"\nProcessing contact form...")

# Call the handler
success, form = _handle_contact_form(request)

print(f"\nResult: {'✓ SUCCESS' if success else '✗ FAILED'}")
print("\nEmail Flow:")
print("  1. ✓ Confirmation email should be sent to: testuser@example.com")
print("  2. ✓ Notification email should be sent to: saharun2056@gmail.com")
print(f"\nCheck your Gmail inbox to verify both emails arrived!")
print("=" * 70)
