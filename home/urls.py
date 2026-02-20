from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),

    # Custom Admin Panel
    path('panel/', views.admin_login, name='admin_login'),
    path('panel/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('panel/logout/', views.admin_logout, name='admin_logout'),
    path('panel/<str:model_name>/add/', views.admin_add, name='admin_add'),
    path('panel/<str:model_name>/edit/<int:pk>/', views.admin_edit, name='admin_edit'),
    path('panel/<str:model_name>/delete/<int:pk>/', views.admin_delete, name='admin_delete'),
]
