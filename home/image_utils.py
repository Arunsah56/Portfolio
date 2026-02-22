"""
Image optimization utilities for efficient image handling
"""
from io import BytesIO
from PIL import Image
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import os


def optimize_image(image_file, max_width=1200, max_height=1200, quality=85):
    """
    Optimize and compress image while maintaining aspect ratio.
    
    Args:
        image_file: Django ImageField file
        max_width: Maximum width in pixels
        max_height: Maximum height in pixels
        quality: JPEG quality (1-100)
    
    Returns:
        Optimized Image file
    """
    img = Image.open(image_file)
    
    # Convert RGBA to RGB if needed (for JPEG compatibility)
    if img.mode in ('RGBA', 'LA', 'P'):
        # Create white background
        background = Image.new('RGB', img.size, (255, 255, 255))
        background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
        img = background
    
    # Calculate new dimensions maintaining aspect ratio
    img.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
    
    # Save to BytesIO buffer
    buffer = BytesIO()
    img.save(buffer, format='JPEG', quality=quality, optimize=True)
    buffer.seek(0)
    
    return buffer


def get_optimized_image_name(original_filename):
    """Generate optimized image filename"""
    name, ext = os.path.splitext(original_filename)
    return f"{name}_optimized.jpg"


def compress_and_optimize_profile_image(image_file, filename):
    """
    Main function to compress and optimize profile picture.
    
    Args:
        image_file: Django file object
        filename: Original filename
    
    Returns:
        Tuple of (optimized_file, new_filename)
    """
    optimized_buffer = optimize_image(image_file)
    optimized_filename = get_optimized_image_name(filename)
    optimized_file = ContentFile(optimized_buffer.getvalue(), name=optimized_filename)
    
    return optimized_file, optimized_filename
