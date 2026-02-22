from django.db import models
from django.core.files.base import ContentFile
from .validators import validate_profile_image
from .image_utils import compress_and_optimize_profile_image
import os


class Profile(models.Model):
    profile_picture = models.ImageField(
        upload_to='profile/',
        blank=True,
        null=True,
        validators=[validate_profile_image],
        help_text='Upload a profile picture (JPG, PNG, GIF, WebP). Max 5MB, recommended 200x200px or larger.'
    )
    file_size = models.PositiveIntegerField(default=0, help_text='File size in bytes', editable=False)
    image_width = models.PositiveIntegerField(default=0, editable=False)
    image_height = models.PositiveIntegerField(default=0, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Profile'

    def __str__(self):
        return "Your Profile Picture"

    def get_file_size_kb(self):
        """Get file size in KB"""
        if self.file_size:
            return round(self.file_size / 1024, 2)
        return 0

    def get_dimensions_display(self):
        """Get image dimensions as string"""
        if self.image_width and self.image_height:
            return f"{self.image_width}x{self.image_height}px"
        return "Unknown"

    def save(self, *args, **kwargs):
        # Ensure only one profile exists
        if not self.pk and Profile.objects.exists():
            self.pk = Profile.objects.first().pk
        
        # Optimize and compress image if a new one is uploaded
        if self.profile_picture:
            # Validate image before processing
            validate_profile_image(self.profile_picture)
            
            # Optimize and compress
            from PIL import Image
            img = Image.open(self.profile_picture)
            self.image_width = img.width
            self.image_height = img.height
            
            # Only compress if file is relatively large
            original_size = self.profile_picture.size
            if original_size > 500 * 1024:  # If larger than 500KB
                optimized_file, optimized_filename = compress_and_optimize_profile_image(
                    self.profile_picture,
                    self.profile_picture.name
                )
                self.profile_picture.save(
                    optimized_filename,
                    optimized_file,
                    save=False
                )
            
            # Update file size
            self.file_size = self.profile_picture.size
        
        super().save(*args, **kwargs)

    def delete_old_image(self):
        """Delete old image file when updating"""
        try:
            if self.pk:
                old_profile = Profile.objects.get(pk=self.pk)
                if old_profile.profile_picture and old_profile.profile_picture != self.profile_picture:
                    old_profile.profile_picture.delete(save=False)
        except Profile.DoesNotExist:
            pass


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
    date_created = models.DateField(auto_now_add=True)
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
