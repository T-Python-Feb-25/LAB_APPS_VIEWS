from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random, string

def home_view(request : HttpRequest):
    content = "Hello World, This is my new HOME for Car Rentals Website ! we're excited to welcome you here."
    return HttpResponse(content)

def about_view(request : HttpRequest):
    content = ("Car rentals provide a convenient way for travelers and locals to access vehicles for short-term use. Customers can book online or in person,choosing options like insurance coverage and fuel policies,"
               " Renting a car allows flexibility in travel without the long-term commitment of ownership.")
    return HttpResponse(content)

def password_generator_view(request : HttpRequest):
    pass1 = string.ascii_letters + string.digits + '!@#$%^&*'

    return HttpResponse(random.choice(pass1) for _ in range(10))

