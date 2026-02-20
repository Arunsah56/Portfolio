# 🌐 Arun's Portfolio Website

A full-featured Django portfolio website built with Django REST Framework, featuring dynamic project showcases, blog posts, experience tracking, and a contact management system with email notifications.

---

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Project Structure](#-project-structure)
- [Database Models](#-database-models)
- [Features Overview](#-features-overview)
- [Admin Panel](#-admin-panel)
- [API Endpoints](#-api-endpoints)
- [Running the Project](#-running-the-project)
- [Email Configuration](#-email-configuration)
- [Troubleshooting](#-troubleshooting)
- [Deployment](#-deployment)

---

## 📸 Screenshots

### Home Page
Your portfolio's stunning hero section with call-to-action buttons
![Home Page](screenshots/home.png)

### Contact Form
Responsive contact form where visitors can reach out
![Contact Form](screenshots/contact.png)

### Admin Dashboard
Custom-built admin panel for managing all content
![Admin Dashboard](screenshots/admin-dashboard.png)

### Email Confirmation
Beautiful HTML email confirmation sent to visitors
![Email Confirmation](screenshots/email-confirmation.png)

---

## ✨ Features

### Public Features
- **Home Page**: Displays hero section, projects, experiences, education, and testimonials
- **About Page**: Detailed information about the portfolio owner
- **Projects Showcase**: Display of portfolio projects with descriptions and images
- **Blog Section**: Published blog posts and articles
- **Contact Form**: Visitor contact form with email validation
  - Saves messages to database
  - Sends admin notification email
  - Sends confirmation email to visitor

### Admin Features
- **Secure Admin Authentication**: Staff-only access with login credentials
- **Dashboard**: Overview of all content with quick stats
- **CRUD Operations** for:
  - Projects (with image uploads)
  - Blog Posts (with markdown support)
  - Experience/Work History
  - Education Records
  - Contact Messages (view only)
- **Responsive Admin Interface**: Clean, modern admin template

### Technical Features
- **REST API**: Full REST API with DRF (Django REST Framework)
- **API Documentation**: Interactive API docs with DRF Spectacular
- **Email Notifications**: Gmail SMTP integration for automated emails
- **Logging**: Comprehensive logging system for debugging
- **Static & Media Files**: Proper handling of CSS, JavaScript, and uploaded images
- **Database**: SQLite for development, configurable for production

---

## 🛠 Tech Stack

- **Backend**: Django 6.0.2
- **Database**: SQLite3
- **API**: Django REST Framework 3.16.1
- **API Documentation**: DRF Spectacular 0.29.0
- **Email**: Gmail SMTP
- **Environment Management**: python-decouple
- **Image Processing**: Pillow 12.1.1
- **Frontend**: HTML5, CSS3, JavaScript

---

## 📦 Prerequisites

- **Python 3.8+** (tested with Python 3.14)
- **pip** (Python package manager)
- **Git** (for version control)
- **Gmail Account** (with App Password enabled for email functionality)
- **Virtual Environment** (recommended)

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Portfolio
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**Current Dependencies:**
- Django==6.0.2
- djangorestframework==3.16.1
- drf-spectacular==0.29.0
- python-decouple==3.8
- Pillow==12.1.1
- asgiref==3.11.1
- sqlparse==0.5.5
- tzdata==2025.3

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Create Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

Follow prompts to set username, email, and password.

---

## ⚙️ Configuration

### 1. Environment Variables (.env file)

Create a `.env` file in the project root:

```dotenv
# Django Settings
SECRET_KEY='your-django-secret-key-here'

# Email Configuration (Gmail SMTP)
EMAIL_HOST_USER='your-email@gmail.com'
EMAIL_HOST_PASSWORD='your-app-password-here'
```

**Important**: Use an **App Password**, not your regular Gmail password!

### 2. Gmail App Password Setup

1. Go to [Google Account Security](https://myaccount.google.com/security)
2. Enable **2-Step Verification** (if not already enabled)
3. Go to [App Passwords](https://myaccount.google.com/apppasswords)
4. Select **Mail** and **Windows Computer** (or your device)
5. Copy the 16-character password (**remove spaces** when adding to .env)
6. Update `.env` file with the password

**Example:**
```
Provided: gxah axmk ywjg trnh
Add to .env: gxahaxmkywjgtrnh
```

### 3. Settings Configuration

Key settings in `Portfolio/settings.py`:

```python
# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = config('EMAIL_HOST_USER')

# Static & Media Files
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Installed Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'rest_framework',
    'drf_spectacular',
]
```

---

## 📁 Project Structure

```
Portfolio/
├── Portfolio/                  # Main project configuration
│   ├── __init__.py
│   ├── settings.py            # Django settings
│   ├── urls.py                # Root URL configuration
│   ├── asgi.py                # ASGI config
│   └── wsgi.py                # WSGI config
│
├── home/                       # Main Django app
│   ├── models.py              # Database models
│   ├── views.py               # View functions
│   ├── api_views.py           # REST API views
│   ├── serializers.py         # DRF serializers
│   ├── forms.py               # Django forms
│   ├── admin_forms.py         # Custom admin forms
│   ├── urls.py                # App URL routing
│   ├── api_urls.py            # API URL routing
│   ├── admin.py               # Admin customization
│   ├── tests.py               # Unit tests
│   ├── management/
│   │   └── commands/
│   │       └── test_email.py  # Email testing command
│   ├── migrations/            # Database migrations
│   └── templatetags/
│       └── custom_filters.py  # Custom template filters
│
├── templates/
│   └── main/
│       ├── base.html          # Base template
│       ├── home.html          # Home page
│       ├── about.html         # About page
│       ├── projects.html      # Projects page
│       ├── blog.html          # Blog page
│       ├── contact.html       # Contact page
│       ├── navbar.html        # Navigation bar
│       ├── footer.html        # Footer
│       ├── admin_login.html   # Admin login
│       ├── admin_dashboard.html
│       ├── admin_form.html
│       ├── admin_delete.html
│       └── emails/
│           └── confirmations_email.html  # Confirmation email template
│
├── static/
│   └── main/
│       ├── css/
│       │   ├── style.css      # Main styles
│       │   └── admin.css      # Admin styles
│       ├── js/
│       │   └── script.js      # JavaScript
│       ├── images/            # Static images
│       └── resume/            # Resume files
│
├── media/
│   └── projects/              # Uploaded project images
│
├── logs/                       # Application logs
│   └── django.log
│
├── tools/                      # Development tools & scripts
│   ├── test_email.py
│   ├── test_contact_form.py
│   └── request_home.py
│
├── manage.py                   # Django management script
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (not in git)
├── .gitignore                  # Git ignore rules
├── db.sqlite3                  # SQLite database
├── EMAIL_SETUP_GUIDE.md       # Email configuration guide
└── README.md                   # This file
```

---

## 🗄️ Database Models

### Contact Message
```python
class ContactMessage:
    name: CharField (max 100)
    email: EmailField
    message: TextField
    created_at: DateTimeField (auto_now_add)
```

### Project
```python
class Project:
    title: CharField
    description: TextField
    technologies: CharField
    image: ImageField
    link: URLField
    github_link: URLField (optional)
    created_at: DateTimeField
    updated_at: DateTimeField
```

### Blog
```python
class Blog:
    title: CharField
    slug: SlugField
    content: TextField
    author: CharField
    featured_image: ImageField
    is_published: BooleanField
    created_at: DateTimeField
    updated_at: DateTimeField
```

### Experience
```python
class Experience:
    title: CharField
    company: CharField
    description: TextField
    start_date: DateField
    end_date: DateField (optional)
    is_current: BooleanField
```

### Education
```python
class Education:
    institution: CharField
    degree: CharField
    field: CharField
    start_year: IntegerField
    end_year: IntegerField
    details: TextField (optional)
```

---

## 🎯 Features Overview

### Contact Form Email Workflow

1. **Visitor fills contact form**
   - Name, email, and message validation
   
2. **Message is saved** to database immediately
   
3. **Admin notification email** is sent to `EMAIL_HOST_USER`
   - Contains visitor details and message
   - HTML formatted email
   
4. **Confirmation email** is sent to visitor
   - HTML formatted thank you email
   - Assures visitor their message was received

5. **User feedback**
   - Success message if both emails sent
   - Warning message if message saved but email failed
   - Error message if form validation fails

### Logging
All email operations are logged to `logs/django.log`:
- Successful email sends
- Failed email attempts with error details
- Email configuration test results

---

## 🔐 Admin Panel

### Access Admin Panel
1. Go to `/admin/` URL
2. Enter superuser credentials

### Or Custom Admin Dashboard
1. Go to `/admin-login/` 
2. Enter staff account credentials
3. Access custom-built admin dashboard with:
   - Message count
   - Project management
   - Blog management
   - Experience tracking
   - Education records
   - Contact message viewing

### Admin Operations

**Projects**
- Add/Edit/Delete projects
- Upload project images
- Add project links and GitHub URLs

**Blog Posts**
- Create/Edit/Delete blog posts
- Mark as published/unpublished
- Add featured images

**Experience**
- Add work experience
- Track employment dates
- Mark current employment

**Education**
- Add education records
- Store institution and degree info
- Track graduation years

**Messages**
- View all contact messages
- See message timestamps
- Search and filter messages

---

## 🔌 API Endpoints

API Base URL: `/api/`

### REST Endpoints (DRF)

**Projects**
- `GET /api/projects/` - List all projects
- `GET /api/projects/{id}/` - Get project details
- `POST /api/projects/` - Create project (admin only)
- `PUT /api/projects/{id}/` - Update project (admin only)
- `DELETE /api/projects/{id}/` - Delete project (admin only)

**Blog Posts**
- `GET /api/blogs/` - List published blogs
- `GET /api/blogs/{id}/` - Get blog details
- `POST /api/blogs/` - Create blog (admin only)
- `PUT /api/blogs/{id}/` - Update blog (admin only)
- `DELETE /api/blogs/{id}/` - Delete blog (admin only)

**Experience**
- `GET /api/experiences/` - List experiences
- `GET /api/experiences/{id}/` - Get experience details

**Education**
- `GET /api/educations/` - List education records
- `GET /api/educations/{id}/` - Get education details

### API Documentation
- Interactive API documentation: `/api/schema/swagger-ui/`
- ReDoc documentation: `/api/schema/redoc/`
- OpenAPI schema: `/api/schema/`

---
## 🔄 GitHub Workflows (CI/CD)

This project includes automated GitHub Actions workflows for continuous integration and continuous deployment.

### Available Workflows

#### 1. **Django Tests** (`.github/workflows/tests.yml`)
Automatically runs on every push and pull request:
- ✅ Runs Django tests across Python 3.8, 3.9, 3.10, 3.11
- ✅ Executes database migrations
- ✅ Generates code coverage reports
- ✅ Uploads coverage to Codecov

**Triggers:**
```
- Push to main or develop branches
- Pull requests to main or develop branches
```

**What it does:**
```bash
✓ Django system checks
✓ Database migrations
✓ Run all tests with pytest
✓ Generate coverage report
✓ Upload to Codecov
```

#### 2. **Code Quality & Linting** (`.github/workflows/linting.yml`)
Checks code style and quality:
- ✅ Black - Code formatting
- ✅ isort - Import sorting  
- ✅ Flake8 - PEP 8 compliance
- ✅ Bandit - Security vulnerabilities

**Triggers:** Push and pull requests to main/develop branches

#### 3. **Django System Checks** (`.github/workflows/django-checks.yml`)
Validates Django configuration:
- ✅ Django system checks
- ✅ Missing migrations detection
- ✅ Static files verification
- ✅ Settings validation

**Triggers:** Push and pull requests to main/develop branches

#### 4. **Deployment** (`.github/workflows/deploy.yml`)
Automatic production deployment (requires configuration):
- ✅ Deployable on main branch push
- ✅ Manual trigger via GitHub Actions UI
- ✅ Requires SSH deployment secrets

**Required Secrets for Deployment:**
```
DEPLOY_KEY      - SSH private key for server access
DEPLOY_HOST     - Server hostname/IP
DEPLOY_USER     - SSH username
DEPLOY_PATH     - Application path on server
```

### Setting Up Secrets for Deployment

1. Go to your GitHub repository settings
2. Navigate to **Settings → Secrets and variables → Actions**
3. Click **New repository secret**
4. Add these secrets:

```
DEPLOY_KEY = (your SSH private key)
DEPLOY_HOST = your-server.com
DEPLOY_USER = ubuntu
DEPLOY_PATH = /home/ubuntu/Portfolio
```

### How to Use Workflows

#### View Workflow Status
1. Go to the **Actions** tab on GitHub
2. See all workflow runs
3. Click on a workflow to view details

#### Manually Trigger Deployment
1. Go to **Actions** tab
2. Select **Deploy to Production**
3. Click **Run workflow**
4. Select branch and confirm

#### Disable a Workflow
1. Go to workflow file in `.github/workflows/`
2. Comment out the `on:` section, or
3. Delete the workflow file

### Local Testing (Before Pushing)

Run tests locally before pushing:

```bash
# Install testing dependencies
pip install pytest pytest-django pytest-cov

# Run tests
pytest

# Run with coverage report
pytest --cov=home --cov-report=html
```

### Adding Tests to Your Project

Create test files in `home/tests.py`:

```python
# home/tests.py
from django.test import TestCase
from .models import Project

class ProjectModelTest(TestCase):
    def test_project_creation(self):
        project = Project.objects.create(
            title='Test Project',
            description='Test Description',
            tech_stack='Django, Python'
        )
        self.assertEqual(project.title, 'Test Project')
```

### GitHub Actions Badge

Add this to your README to show workflow status:

```markdown
![Tests](https://github.com/YOUR_USERNAME/Portfolio/workflows/Django%20Tests/badge.svg)
![Linting](https://github.com/YOUR_USERNAME/Portfolio/workflows/Code%20Quality%20%26%20Linting/badge.svg)
```

Replace `YOUR_USERNAME` with your GitHub username.

---
## ▶️ Running the Project

### Start Django Development Server

```bash
python manage.py runserver
```

Server runs at: `http://127.0.0.1:8000/`

### Access Different Pages

- **Home**: http://localhost:8000/
- **About**: http://localhost:8000/about/
- **Projects**: http://localhost:8000/projects/
- **Blog**: http://localhost:8000/blog/
- **Contact**: http://localhost:8000/contact/
- **Admin**: http://localhost:8000/admin/
- **Custom Admin**: http://localhost:8000/admin-login/
- **API Docs**: http://localhost:8000/api/schema/swagger-ui/

### Test Email Configuration

```bash
python manage.py test_email
```

This command will:
- Display email configuration
- Test SMTP connection to Gmail
- Test Gmail authentication
- Attempt to send test email
- Show success/error messages with solutions

---

## 💌 Email Configuration

### How It Works

1. **Contact form submission** triggers email sending
2. **Two emails are sent**:
   - **Admin notification**: Notifies you of new message
   - **Confirmation email**: Confirms receipt to visitor

3. **Error handling**:
   - Message always saved to database first
   - Email failures don't prevent message saving
   - Users are informed if email delivery fails

### Email Template

Default confirmation email template: `templates/main/emails/confirmations_email.html`

```html
<!-- Customize this template to match your branding -->
<h2>Thank You for Reaching Out!</h2>
<p>Hi {{ name }},</p>
<p>Your message has been received and will be reviewed soon.</p>
```

### Troubleshooting Email

**Error: "Username and Password not accepted"**
- Use **App Password**, not regular Gmail password
- Remove spaces from password in .env
- Ensure 2-Factor Authentication is enabled on Gmail account
- Generate new App Password from Google Account

**Test Email Feature**
```bash
python manage.py test_email --recipient alternate@email.com
```

---

## 🐛 Troubleshooting

### Common Issues

#### 1. ModuleNotFoundError
**Problem**: Missing package
```
ModuleNotFoundError: No module named 'django'
```

**Solution**:
```bash
pip install -r requirements.txt
```

#### 2. Email Authentication Failed
**Problem**: "Username and Password not accepted"

**Solution**:
- Use Gmail App Password (not regular password)
- Enable 2-Factor Authentication on Gmail
- Remove spaces from password in .env file
- Restart Django server after updating .env

#### 3. Database Issues
**Problem**: "No such table: home_project"

**Solution**:
```bash
python manage.py migrate
```

#### 4. Static Files Not Loading
**Problem**: CSS/JS not loading on page

**Solution**:
```bash
python manage.py collectstatic
```

#### 5. Cannot Access Admin
**Problem**: "Page not found" at /admin/

**Solution**:
- Ensure superuser created: `python manage.py createsuperuser`
- Check user is_staff and is_superuser flags

### Debug Mode

Enable detailed error messages (development only):

In `Portfolio/settings.py`:
```python
DEBUG = True  # Set to False for production
ALLOWED_HOSTS = ['*']  # Set specific hosts for production
```

---

## 🚢 Deployment

### Before Deploying

1. **Set DEBUG = False** in settings.py
```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
```

2. **Collect static files**
```bash
python manage.py collectstatic --noinput
```

3. **Use production database** (PostgreSQL recommended)
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'portfolio_db',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

4. **Use production email settings** (already configured via .env)

5. **Enable HTTPS**
```python
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

### Hosting Options

- **Heroku**: Free tier available
- **PythonAnywhere**: Easy Django hosting
- **AWS**: EC2 or Elastic Beanstalk
- **DigitalOcean**: Affordable VPS
- **Vercel**: For frontend (static files)

### Production WSGI Server

Install gunicorn:
```bash
pip install gunicorn
```

Run with gunicorn:
```bash
gunicorn Portfolio.wsgi:application --bind 0.0.0.0:8000
```

---

## 📝 License

This project is open source and available under the MIT License.

---

## 👤 Author

**Arun Sah**
- Portfolio: Your domain here
- Email: saharun2056@gmail.com
- GitHub: Your GitHub profile link

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📞 Support

For support, email saharun2056@gmail.com or open an issue on GitHub.

---

## 🎉 Acknowledgements

- Django documentation
- Django REST Framework
- DRF Spectacular for API docs
- All contributors and users 

