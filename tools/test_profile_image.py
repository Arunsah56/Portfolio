"""
Test profile picture upload and optimization
"""
import os
import django
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Portfolio.settings')
django.setup()

from home.models import Profile
from home.image_utils import optimize_image, compress_and_optimize_profile_image
from home.validators import validate_profile_image


class ProfileImageTests(TestCase):
    """Test profile picture upload and optimization"""

    def setUp(self):
        """Create test profile"""
        self.profile = Profile.objects.create()

    def create_test_image(self, width=800, height=800, format='JPEG', size_kb=None):
        """
        Create a test image file
        
        Args:
            width: Image width in pixels
            height: Image height in pixels
            format: Image format (JPEG, PNG, etc.)
            size_kb: Optional size in KB to simulate
        """
        # Create image
        img = Image.new('RGB', (width, height), color='blue')
        
        # Save to BytesIO
        buffer = BytesIO()
        img.save(buffer, format=format)
        buffer.seek(0)
        
        # Create uploaded file
        filename = f'test_image_{width}x{height}.{format.lower()}'
        return SimpleUploadedFile(
            filename,
            buffer.getvalue(),
            content_type=f'image/{format.lower()}'
        )

    def test_image_optimization(self):
        """Test image optimization reduces file size"""
        print("\n✓ Test: Image Optimization")
        
        # Create a large image (1600x1600)
        large_img = self.create_test_image(width=1600, height=1600)
        original_size = large_img.size
        
        # Optimize
        optimized = optimize_image(large_img)
        optimized_size = len(optimized.getvalue())
        
        print(f"  Original size: {original_size / 1024:.2f} KB")
        print(f"  Optimized size: {optimized_size / 1024:.2f} KB")
        print(f"  Reduction: {((original_size - optimized_size) / original_size * 100):.1f}%")
        
        # Assert optimization worked
        assert optimized_size < original_size, "Optimized image should be smaller"
        print("  ✅ Optimization working correctly")

    def test_image_validation(self):
        """Test image validation"""
        print("\n✓ Test: Image Validation")
        
        # Test valid image
        valid_img = self.create_test_image(width=800, height=800)
        try:
            validate_profile_image(valid_img)
            print("  ✅ Valid image passed validation")
        except Exception as e:
            print(f"  ❌ Valid image failed: {e}")
            raise

    def test_small_image_validation(self):
        """Test small image is rejected"""
        print("\n✓ Test: Small Image Validation")
        
        # Test too small image
        small_img = self.create_test_image(width=100, height=100)
        try:
            validate_profile_image(small_img)
            print("  ❌ Should have rejected small image")
            assert False
        except Exception as e:
            print(f"  ✅ Correctly rejected small image: {str(e)[:60]}...")

    def test_profile_save_with_image(self):
        """Test profile save with image"""
        print("\n✓ Test: Profile Save with Image")
        
        test_img = self.create_test_image(width=1000, height=1000)
        
        # Assign and save
        self.profile.profile_picture = test_img
        self.profile.save()
        
        # Check metadata
        assert self.profile.image_width == 1000, f"Width should be 1000, got {self.profile.image_width}"
        assert self.profile.image_height == 1000, f"Height should be 1000, got {self.profile.image_height}"
        assert self.profile.file_size > 0, "File size should be recorded"
        
        print(f"  Image dimensions: {self.profile.image_width}x{self.profile.image_height}")
        print(f"  File size: {self.profile.get_file_size_kb()} KB")
        print("  ✅ Profile saved successfully with metadata")


if __name__ == '__main__':
    print("\n" + "="*60)
    print("PROFILE PICTURE OPTIMIZATION TEST SUITE")
    print("="*60)
    
    # Run tests
    test_suite = ProfileImageTests()
    test_suite.setUp()
    
    try:
        test_suite.test_image_optimization()
        test_suite.test_image_validation()
        test_suite.test_small_image_validation()
        test_suite.test_profile_save_with_image()
        
        print("\n" + "="*60)
        print("✅ ALL TESTS PASSED!")
        print("="*60 + "\n")
    except Exception as e:
        print(f"\n❌ TEST FAILED: {e}\n")
        raise
