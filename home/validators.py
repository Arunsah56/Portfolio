"""
Custom validators for profile picture uploads
"""
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
import os


# Maximum file size: 5MB
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

# Allowed image formats
ALLOWED_FORMATS = {'jpeg', 'jpg', 'png', 'gif', 'webp'}

# Minimum dimensions
MIN_WIDTH = 200
MIN_HEIGHT = 200

# Maximum dimensions
MAX_WIDTH = 4000
MAX_HEIGHT = 4000


def validate_profile_image(image_file):
    """
    Validate profile image file.
    
    Checks:
    - File size (max 5MB)
    - File format (must be image)
    - Image dimensions (200x200 to 4000x4000)
    
    Raises:
        ValidationError if validation fails
    """
    # Check file size
    if image_file.size > MAX_FILE_SIZE:
        raise ValidationError(
            f'Image file too large. Maximum size is 5MB. Your file is {image_file.size / (1024*1024):.2f}MB.'
        )
    
    # Check file extension
    ext = os.path.splitext(image_file.name)[1][1:].lower()
    if ext not in ALLOWED_FORMATS:
        raise ValidationError(
            f'Invalid image format. Allowed formats: {", ".join(ALLOWED_FORMATS)}'
        )
    
    # Check image dimensions
    try:
        width, height = get_image_dimensions(image_file)
        
        if width is None or height is None:
            raise ValidationError('Unable to determine image dimensions. Please upload a valid image.')
        
        if width < MIN_WIDTH or height < MIN_HEIGHT:
            raise ValidationError(
                f'Image is too small. Minimum dimensions: {MIN_WIDTH}x{MIN_HEIGHT}px. Your image: {width}x{height}px'
            )
        
        if width > MAX_WIDTH or height > MAX_HEIGHT:
            raise ValidationError(
                f'Image is too large. Maximum dimensions: {MAX_WIDTH}x{MAX_HEIGHT}px. Your image: {width}x{height}px'
            )
    except Exception as e:
        if isinstance(e, ValidationError):
            raise
        raise ValidationError(f'Error validating image: {str(e)}')
