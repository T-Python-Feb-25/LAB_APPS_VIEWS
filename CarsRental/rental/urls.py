from django.urls import path
from . import views

app_name = "rental"

urlpatterns = [
    path("", views.page_view, name="page_view"),
    path("about/", views.about_view, name="about_view"),
    path("password/generate/", views.generate_pas, name="generate_pas")
]