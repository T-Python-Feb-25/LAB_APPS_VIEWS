# home/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page content
    path('about/', views.about, name='about'),  # About page content
    path('password/generate/', views.generate_password, name='generate_password'),  # New password generation URL
]
