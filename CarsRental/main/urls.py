from django.urls import path
from . import views
from django.http import JsonResponse



main = "main"

urlpatterns = [
path("path/to/view/", views.page_view, name="page_view"),
path("", views.page_main, name="page_main"),
path("about/", views.page_about, name="page_about"),
path("password/generate/", views.page_bouns, name="page_bouns"),
]

