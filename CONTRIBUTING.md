# Contributing to Arun's Portfolio

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to this project.

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on the code, not the person
- Welcome diverse perspectives

## Getting Started

### 1. Fork the Repository
Click the "Fork" button on GitHub to create your own copy.

### 2. Clone Your Fork
```bash
git clone https://github.com/YOUR_USERNAME/Portfolio.git
cd Portfolio
```

### 3. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
pip install pytest pytest-django black flake8 isort
```

### 5. Create a Branch
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

## Making Changes

### Code Style
This project follows PEP 8 guidelines with some variations:

- **Line length**: Max 120 characters
- **Format**: Use Black for consistent formatting
- **Imports**: Use isort for import organization
- **Linting**: Ensure flake8 compliance

### Format Your Code
```bash
# Format with Black
black .

# Sort imports
isort .

# Check linting
flake8 . --max-line-length=120
```

### Writing Tests
All new features should include tests:

```python
# home/tests.py
from django.test import TestCase
from .models import Project

class ProjectTestCase(TestCase):
    def setUp(self):
        Project.objects.create(
            title='Test',
            description='Test',
            tech_stack='Django'
        )
    
    def test_project_creation(self):
        project = Project.objects.get(title='Test')
        self.assertEqual(project.title, 'Test')
```

Run tests locally:
```bash
pytest
# or
python manage.py test
```

## Commit Guidelines

### Commit Message Format
```
<type>: <subject>

<body>

<footer>
```

### Types
- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting)
- **refactor**: Code refactoring
- **perf**: Performance improvements
- **test**: Adding or updating tests

### Examples
```
feat: Add project filtering by technology

fix: Resolve email sending error on contact form

docs: Update README with new screenshots

test: Add unit tests for Project model
```

## Submitting Changes

### 1. Sync with Upstream
```bash
git fetch origin
git rebase origin/main
```

### 2. Push to Your Fork
```bash
git push origin feature/your-feature-name
```

### 3. Create a Pull Request
- Go to GitHub and create a Pull Request
- Fill out the PR template completely
- Link any related issues
- Request review from maintainers

### 4. Respond to Feedback
- Address requested changes promptly
- Keep commits clean and logical
- Maintain respectful communication

## Pull Request Checklist

Before submitting, ensure:
- [ ] Code follows project style guide
- [ ] All tests pass locally
- [ ] No new warnings generated
- [ ] Documentation updated
- [ ] Commit messages are clear
- [ ] Changes are focused and atomic
- [ ] PR description is complete

## Review Process

1. **Automated Checks**
   - GitHub Actions runs tests
   - Code quality checks pass
   - Coverage maintained or improved

2. **Code Review**
   - At least one maintainer reviews
   - Feedback addressed promptly
   - Discussions resolved

3. **Merge**
   - PR approved and all checks pass
   - Branch squashed and merged into main

## Issue Guidelines

### Reporting Bugs
Use the bug report template and include:
- Clear description of the issue
- Steps to reproduce
- Expected vs actual behavior
- Environment details
- Error logs

### Requesting Features
Use the feature request template and include:
- Clear description of desired feature
- Use cases and benefits
- Proposed implementation (optional)
- Priority assessment

## Development Tips

### Running the Server
```bash
python manage.py runserver
```

### Testing Email
```bash
python manage.py test_email
```

### Creating Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Testing Admin Panel
```bash
python manage.py createsuperuser
# Then visit http://localhost:8000/admin/
```

## Project Structure
```
Portfolio/
├── .github/          # GitHub workflows and templates
├── home/             # Django app
├── templates/        # HTML templates
├── static/           # CSS, JS, images
├── manage.py         # Django CLI
├── requirements.txt  # Dependencies
└── README.md         # Project documentation
```

## Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [PEP 8 Style Guide](https://pep8.org/)
- [GitHub Guides](https://guides.github.com/)
- [Git Documentation](https://git-scm.com/doc)

## Questions?

- Open an issue for bug reports
- Use discussions for questions
- Check existing issues first

## Recognition

Contributors will be recognized in:
- README file
- GitHub contributor graph
- Project history

Thank you for contributing! 🎉
