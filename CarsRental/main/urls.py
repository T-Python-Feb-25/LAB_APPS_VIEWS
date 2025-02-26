from django.urls import path
from . import views

name_app= "main"


urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("about/",views.about_view, name="about_view"), 
    path("password/generate/", views.password_generate, name= "password_generate")
    

    
]
