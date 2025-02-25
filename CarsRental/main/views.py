from django.shortcuts import render
from django.http import HttpRequest ,HttpResponse
import random
import string

# Create your views here.

def home_view(request :HttpRequest):
    content="Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here."
    return HttpResponse (content)

def about_us_view(request :HttpRequest):
    content="Our company is one of the most promising companies in the market and this comes from our great interest in the satisfaction and comfort of our customers "
    return HttpResponse(content)

def password_view(request :HttpRequest):
    characters=string.ascii_letters + string.digits+string.punctuation
    password=''.join(random.choice(characters) for i in range(10))
    return HttpResponse(password)