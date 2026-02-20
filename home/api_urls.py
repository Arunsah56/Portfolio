from django.urls import path
from . import api_views

urlpatterns = [
    path('projects/', api_views.ProjectListAPI.as_view(), name='api-projects'),
    path('experiences/', api_views.ExperienceListAPI.as_view(), name='api-experiences'),
    path('educations/', api_views.EducationListAPI.as_view(), name='api-educations'),
    path('blogs/', api_views.BlogListAPI.as_view(), name='api-blogs'),
    path('contact/', api_views.ContactCreateAPI.as_view(), name='api-contact'),
]
