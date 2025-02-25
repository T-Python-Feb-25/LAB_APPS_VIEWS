from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("about/", views.about_view, name="about_view"),
    path('', views.generate_password, name='home'),
    path('password/generate/', views.generate_password, name='generate_password'),
]