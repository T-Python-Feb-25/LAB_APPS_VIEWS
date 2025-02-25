from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
 # Create your views here.
def page_view(request : HttpRequest):
    content = "Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here."
    return HttpResponse(content)

def about_view(request : HttpRequest):
    content1 = "A simple paragraph about Car Rentals. "
    return HttpResponse(content1)




