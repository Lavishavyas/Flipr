from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('admin-panel/', views.admin_panel),
    path('projects/', views.get_projects),
    path('projects/add/', views.add_project),
    path('clients/', views.get_clients),
    path('clients/add/', views.add_client),
    path('contact/', views.submit_contact),
    path('subscribe/', views.subscribe_email),
]
