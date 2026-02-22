from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Profile, Education, Experience, Project, Blog, ContactMessage
from .admin_forms import ProfileForm


# ─── Site Branding ───────────────────────────────────────────────────────
admin.site.site_title = "Abhay's Portfolio"
admin.site.site_header = "Abhay's Portfolio — Admin"
admin.site.index_title = "Manage Your Content"


# ─── Profile ─────────────────────────────────────────────────────────────
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    form = ProfileForm
    fields = ('profile_picture', 'profile_preview', 'image_info', 'updated_at')
    readonly_fields = ('profile_preview', 'image_info', 'updated_at')

    def profile_preview(self, obj):
        """Display image preview in admin"""
        if obj.profile_picture:
            return format_html(
                '<img src="{}" style="max-width: 300px; max-height: 300px; border-radius: 8px; border: 2px solid #ddd;" />',
                obj.profile_picture.url
            )
        return "No image uploaded"
    profile_preview.short_description = 'Preview'

    def image_info(self, obj):
        """Display image optimization information"""
        if obj.profile_picture:
            info = f"""
            <div style="background-color: #f0f0f0; padding: 15px; border-radius: 5px; font-family: monospace;">
                <strong>Image Information:</strong><br>
                Size: {obj.get_file_size_kb()} KB<br>
                Dimensions: {obj.get_dimensions_display()}<br>
                Updated: {obj.updated_at.strftime('%Y-%m-%d %H:%M:%S')}<br>
                <br>
                <span style="color: green;">✓ Optimized & Compressed</span>
            </div>
            """
            return format_html(info)
        return format_html('<span style="color: #999;">Upload an image to see information</span>')
    image_info.short_description = 'Image Details'

    def has_add_permission(self, request):
        # Allow adding only if no profile exists
        return not Profile.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Prevent deletion
        return False


# ─── Education ───────────────────────────────────────────────────────────
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('institution', 'degree', 'duration', 'order')
    list_editable = ('order',)
    search_fields = ('institution', 'degree')
    ordering = ('order',)


# ─── Experience ──────────────────────────────────────────────────────────
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('organization', 'role', 'duration', 'partner_label', 'order')
    list_editable = ('order',)
    search_fields = ('organization', 'role')
    ordering = ('order',)


# ─── Project ─────────────────────────────────────────────────────────────
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'tech_stack', 'github_link', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'tech_stack')
    ordering = ('order',)


# ─── Blog ────────────────────────────────────────────────────────────────
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_published')
    list_filter = ('is_published', 'created_at')
    list_editable = ('is_published',)
    search_fields = ('title', 'content')
    ordering = ('-created_at',)


# ─── Contact Messages (Read-only) ───────────────────────────────────────
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'short_message', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'message')
    ordering = ('-created_at',)
    readonly_fields = ('name', 'email', 'message', 'created_at')

    def short_message(self, obj):
        return obj.message[:80] + '...' if len(obj.message) > 80 else obj.message
    short_message.short_description = 'Message'

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False