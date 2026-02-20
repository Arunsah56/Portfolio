# Email Configuration Guide

## Current Status
Your Django application is configured to send emails via Gmail SMTP, but **authentication is failing**.

## The Problem
```
SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted')
```

This means your Gmail credentials in `.env` are not correct or not properly set up.

---

## Solution: Generate Gmail App Password

Gmail requires special "App Passwords" when you have **2-Factor Authentication (2FA)** enabled.

### Step 1: Enable 2-Factor Authentication (if not already enabled)
1. Go to your Google Account: https://myaccount.google.com/
2. Click on "Security" in the left menu
3. Enable 2-Step Verification (if not already enabled)

### Step 2: Generate an App Password
1. Go to: https://myaccount.google.com/apppasswords
2. Select **Mail** from the "Select app" dropdown
3. Select **Windows Computer** from the "Select device" dropdown
4. Click **Generate**
5. Google will show you a **16-character password with spaces**
   - Example: `hxub zvgz ibkx hnzc`

### Step 3: Update Your `.env` File
Copy the 16-character password and update your `.env` file:

```dotenv
EMAIL_HOST_USER='saharun2056@gmail.com'
EMAIL_HOST_PASSWORD='hxub zvgz ibkx hnzc'  # <-- Paste the password here
```

### Step 4: Test the Configuration
Run the test command in your terminal:

```bash
python manage.py test_email
```

This will:
- Display your current email configuration
- Test the SMTP connection to Gmail
- Test authentication
- Send a test email to your inbox

## Alternative: Allow Less Secure Apps (Not Recommended)
If you don't want to use App Passwords:

1. Go to: https://myaccount.google.com/lesssecureapps
2. Enable "Allow less secure app access"

⚠️ **Warning:** This is less secure and Google may disable it anytime.

---

## Troubleshooting

### Issue: "SMTPAuthenticationError"
- ✓ Check that you're using the **App Password** (not your main Gmail password)
- ✓ Check that spaces in the password are preserved
- ✓ Run `python manage.py test_email` to verify

### Issue: "Connection refused"
- ✓ Verify Gmail SMTP settings:
  - Host: `smtp.gmail.com`
  - Port: `587`
  - TLS: `enabled`

### Issue: Emails not received
- ✓ Check Google account's "Less secure app" settings
- ✓ Check email spam/junk folder
- ✓ Run `python manage.py test_email` to send a test email

---

## How Email Sending Works in Your App

When a user submits the contact form:

1. **Admin Notification Email**
   - Sent to: `saharun2056@gmail.com`
   - Contains: User's name, email, and message

2. **Confirmation Email to Visitor**
   - Sent to: User's email address
   - Contains: Thank you message with HTML template

3. **Database Storage**
   - Message saved in the database
   - Visible in admin dashboard

---

## Testing

### Run Test Email Command
```bash
python manage.py test_email
```

### Test Contact Form on Website
1. Go to the contact page
2. Fill in the form
3. Submit the form
4. Check the console/logs for:
   - Success messages
   - Error messages (if email fails)

### Check Logs
Logs are saved in: `logs/django.log`

You can view them regularly to monitor email sending status.

---

## Security Notes

- Never commit `.env` file to git
- Keep your App Password confidential
- Use separate App Passwords for different applications
- Regenerate App Passwords if compromised

---

## Support

If you still have issues after following these steps:

1. Run: `python manage.py test_email`
2. Check the error message carefully
3. Share the error details (without password)
4. Review console/logs output

