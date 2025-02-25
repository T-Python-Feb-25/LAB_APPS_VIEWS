from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("about/us/", views.about_view, name="about_view"),
    path("password/generate/", views.password_generate_view, name="password_generate_view")
]
