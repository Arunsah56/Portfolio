"""
Management command to optimize existing profile picture
Usage: python manage.py optimize_profile_image
"""
from django.core.management.base import BaseCommand
from home.models import Profile
from home.image_utils import compress_and_optimize_profile_image
from PIL import Image


class Command(BaseCommand):
    help = 'Optimize and compress the profile picture'

    def handle(self, *args, **options):
        try:
            profile = Profile.objects.first()
            
            if not profile or not profile.profile_picture:
                self.stdout.write(
                    self.style.WARNING('❌ No profile picture found to optimize')
                )
                return
            
            self.stdout.write('🔄 Optimizing profile picture...')
            
            # Get original file info
            original_size = profile.profile_picture.size
            
            # Optimize image
            optimized_file, optimized_filename = compress_and_optimize_profile_image(
                profile.profile_picture,
                profile.profile_picture.name
            )
            
            # Save optimized version
            profile.profile_picture.save(
                optimized_filename,
                optimized_file,
                save=False
            )
            
            # Update image dimensions
            img = Image.open(profile.profile_picture)
            profile.image_width = img.width
            profile.image_height = img.height
            profile.file_size = profile.profile_picture.size
            
            profile.save()
            
            new_size = profile.profile_picture.size
            reduction = ((original_size - new_size) / original_size) * 100 if original_size > 0 else 0
            
            self.stdout.write(self.style.SUCCESS('✓ Profile picture optimized successfully!'))
            self.stdout.write(f'  Original size: {original_size / 1024:.2f} KB')
            self.stdout.write(f'  Optimized size: {new_size / 1024:.2f} KB')
            self.stdout.write(f'  Reduction: {reduction:.1f}%')
            self.stdout.write(f'  Dimensions: {profile.image_width}x{profile.image_height}px')
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Error optimizing profile picture: {str(e)}')
            )
