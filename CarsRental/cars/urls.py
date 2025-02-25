from django.urls import path
from . import views

app_name = "cars"

urlpatterns = [
    path("",views.page1 , name="page1"),
    path("about/",views.page2, name="page2"),
    path("password/generate/",views.bouns, name="bouns")
]