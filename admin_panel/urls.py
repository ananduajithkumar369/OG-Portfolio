from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    # Home
    path('v1/home/', views.dashboard_home, name='dashboard_home'),
    path('v1/home/edit/', views.home_edit, name='dashboard_home_edit'),

    # Academics
    path('v1/academics/', views.academics_list, name='academics_list'),
    path('v1/academics/add/', views.academics_add, name='academics_add'),
    path('v1/academics/<int:pk>/edit/', views.academics_edit, name='academics_edit'),
    path('v1/academics/<int:pk>/delete/', views.academics_delete, name='academics_delete'),

    # Experience
    path('v1/experience/', views.experience_list, name='experience_list'),
    path('v1/experience/add/', views.experience_add, name='experience_add'),
    path('v1/experience/<int:pk>/edit/', views.experience_edit, name='experience_edit'),
    path('v1/experience/<int:pk>/delete/', views.experience_delete, name='experience_delete'),

    # Projects
    path('v1/projects/', views.project_list, name='project_list'),
    path('v1/projects/add/', views.project_add, name='project_add'),
    path('v1/projects/<int:pk>/edit/', views.project_edit, name='project_edit'),
    path('v1/projects/<int:pk>/delete/', views.project_delete, name='project_delete'),

    # Skills
    path('v1/skills/', views.skill_list, name='skill_list'),
    path('v1/skills/add/', views.skill_add, name='skill_add'),
    path('v1/skills/<int:pk>/edit/', views.skill_edit, name='skill_edit'),
    path('v1/skills/<int:pk>/delete/', views.skill_delete, name='skill_delete'),

    # About & Contact
    path('v1/about/edit/', views.about_edit, name='about_edit'),
    path('v1/contact/edit/', views.contact_edit, name='contact_edit'),
    path('v1/contact/messages/', views.contact_messages, name='contact_messages'),
]



