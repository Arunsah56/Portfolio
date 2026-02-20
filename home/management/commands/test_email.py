from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.conf import settings
import smtplib


class Command(BaseCommand):
    help = 'Test email configuration and send a test email'

    def add_arguments(self, parser):
        parser.add_argument(
            '--recipient',
            type=str,
            default=settings.EMAIL_HOST_USER,
            help='Email recipient (default: EMAIL_HOST_USER)',
        )

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('=' * 70))
        self.stdout.write(self.style.SUCCESS('EMAIL CONFIGURATION TEST'))
        self.stdout.write(self.style.SUCCESS('=' * 70))
        
        self.stdout.write(f'Email Backend: {settings.EMAIL_BACKEND}')
        self.stdout.write(f'Email Host: {settings.EMAIL_HOST}')
        self.stdout.write(f'Email Port: {settings.EMAIL_PORT}')
        self.stdout.write(f'Email Use TLS: {settings.EMAIL_USE_TLS}')
        self.stdout.write(f'Email Host User: {settings.EMAIL_HOST_USER}')
        self.stdout.write(f'Default From Email: {settings.DEFAULT_FROM_EMAIL}')
        
        password_display = '*' * len(settings.EMAIL_HOST_PASSWORD) if settings.EMAIL_HOST_PASSWORD else 'NOT SET'
        self.stdout.write(f'Email Host Password Length: {len(settings.EMAIL_HOST_PASSWORD)} characters ({password_display})')
        
        self.stdout.write(self.style.SUCCESS('=' * 70))
        self.stdout.write('')
        
        # Test SMTP connection
        self.stdout.write(self.style.WARNING('Testing SMTP Connection...'))
        try:
            server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
            server.starttls()
            self.stdout.write(self.style.SUCCESS('✓ SMTP connection successful'))
            
            # Test login
            self.stdout.write(self.style.WARNING('Testing Gmail authentication...'))
            server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
            self.stdout.write(self.style.SUCCESS('✓ Gmail authentication successful'))
            server.quit()
            
        except smtplib.SMTPAuthenticationError as e:
            self.stdout.write(self.style.ERROR(f'✗ Authentication failed: {str(e)}'))
            self.stdout.write(self.style.ERROR(''))
            self.stdout.write(self.style.ERROR('SOLUTION: Your Gmail credentials are incorrect.'))
            self.stdout.write(self.style.ERROR(''))
            self.stdout.write(self.style.WARNING('For Gmail with 2-Factor Authentication:'))
            self.stdout.write('  1. Go to: https://myaccount.google.com/apppasswords')
            self.stdout.write('  2. Select "Mail" and "Windows Computer"')
            self.stdout.write('  3. Copy the generated 16-character password')
            self.stdout.write('  4. Update EMAIL_HOST_PASSWORD in .env with the new password')
            self.stdout.write('')
            return
        except smtplib.SMTPException as e:
            self.stdout.write(self.style.ERROR(f'✗ SMTP error: {str(e)}'))
            return
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ Connection error: {str(e)}'))
            return

        # Send test email
        recipient = options['recipient']
        subject = 'Test Email from Django Portfolio'
        message = f'''
This is a test email to verify that email sending is working correctly.

Configuration:
- From: {settings.DEFAULT_FROM_EMAIL}
- To: {recipient}
- Host: {settings.EMAIL_HOST}:{settings.EMAIL_PORT}

If you received this email, congratulations! Your email configuration is working.
        '''.strip()

        self.stdout.write(self.style.WARNING(f'Sending test email to {recipient}...'))
        try:
            result = send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [recipient],
                fail_silently=False,
            )
            self.stdout.write(self.style.SUCCESS(f'✓ Test email sent successfully!'))
            self.stdout.write(f'  Recipient: {recipient}')
            self.stdout.write(f'  Subject: {subject}')
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ Failed to send test email: {str(e)}'))
