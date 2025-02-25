from django.urls import path
from . import views

app_name = "rental"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("about/", views.about_view, name="about"),
    path("password/generate", views.password_view, name="password_view"),
]
