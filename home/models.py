from django.db import models


class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0, help_text='Lower numbers appear first')

    class Meta:
        ordering = ['order']
        verbose_name_plural = 'Education'

    def __str__(self):
        return f'{self.institution} — {self.degree}'


class Experience(models.Model):
    organization = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    description = models.TextField()
    partner_label = models.CharField(
        max_length=200, blank=True,
        help_text='Optional label shown next to org name, e.g. "Partnered with IBM"',
    )
    github_link = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0, help_text='Lower numbers appear first')

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.organization


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0, help_text='Lower numbers appear first')

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True, help_text='Uncheck to save as draft')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
