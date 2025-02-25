from django.urls import path
from . import views
app_name="main"

urlpatterns = [
    path("path/to/view/",views.home_view, name="home_view"),
    path("path/about_us_view/",views.about_us_view, name="about_us_view"),
    path("path/password_view/",views.password_view, name="password_view" ),
]