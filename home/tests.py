from django.test import TestCase
from django.test.client import Client
from .models import Project, Blog, Education, Experience, ContactMessage


class ProjectModelTest(TestCase):
    """Test cases for Project model"""
    
    def setUp(self):
        """Create a test project"""
        self.project = Project.objects.create(
            title='Test Project',
            description='A test project description',
            tech_stack='Django, Python, PostgreSQL',
            github_link='https://github.com/test/project',
            live_link='https://example.com',
            order=1
        )

    def test_project_creation(self):
        """Test that a project can be created"""
        self.assertEqual(self.project.title, 'Test Project')
        self.assertEqual(self.project.description, 'A test project description')

    def test_project_string_representation(self):
        """Test the string representation of a project"""
        self.assertEqual(str(self.project), 'Test Project')


class BlogModelTest(TestCase):
    """Test cases for Blog model"""
    
    def setUp(self):
        """Create a test blog post"""
        self.blog = Blog.objects.create(
            title='Test Blog Post',
            content='This is a test blog post content',
            is_published=True
        )

    def test_blog_creation(self):
        """Test that a blog post can be created"""
        self.assertEqual(self.blog.title, 'Test Blog Post')
        self.assertTrue(self.blog.is_published)

    def test_blog_string_representation(self):
        """Test the string representation of a blog"""
        self.assertEqual(str(self.blog), 'Test Blog Post')


class ContactMessageModelTest(TestCase):
    """Test cases for ContactMessage model"""
    
    def setUp(self):
        """Create a test contact message"""
        self.message = ContactMessage.objects.create(
            name='John Doe',
            email='john@example.com',
            message='This is a test message'
        )

    def test_contact_message_creation(self):
        """Test that a contact message can be created"""
        self.assertEqual(self.message.name, 'John Doe')
        self.assertEqual(self.message.email, 'john@example.com')

    def test_contact_message_string_representation(self):
        """Test the string representation of a contact message"""
        self.assertEqual(str(self.message), 'John Doe')


class HomeViewTests(TestCase):
    """Test cases for home view"""
    
    def setUp(self):
        """Create test data"""
        self.client = Client()
        self.project = Project.objects.create(
            title='Test Project',
            description='Test',
            tech_stack='Django'
        )
        self.blog = Blog.objects.create(
            title='Test Blog',
            content='Test',
            is_published=True
        )

    def test_home_page_loads(self):
        """Test that the home page loads successfully"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_contains_projects(self):
        """Test that home page displays projects"""
        response = self.client.get('/')
        self.assertContains(response, 'Test Project')


class ContactViewTests(TestCase):
    """Test cases for contact view"""
    
    def setUp(self):
        """Setup test client"""
        self.client = Client()

    def test_contact_page_loads(self):
        """Test that the contact page loads"""
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

    def test_contact_form_submit(self):
        """Test submitting a contact form"""
        data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'Test message'
        }
        response = self.client.post('/contact/', data, follow=True)
        # Check that message was saved
        self.assertTrue(ContactMessage.objects.filter(name='Test User').exists())

