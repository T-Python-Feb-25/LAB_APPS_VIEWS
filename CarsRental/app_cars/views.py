from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import secrets
import string

 # Create your views here.
def page_view(request : HttpRequest):
    content = "Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here."
    return HttpResponse(content)

def about_view(request : HttpRequest):
    content1 = "A simple paragraph about Car Rentals. "
    return HttpResponse(content1)

def generate_password(request: HttpRequest):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for r in range(10))
    return HttpResponse(f"Random Password: {password}")



