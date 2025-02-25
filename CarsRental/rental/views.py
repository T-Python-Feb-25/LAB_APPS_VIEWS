from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random
import string


# Create your views here.

def page_view(request:HttpRequest):
    
    return HttpResponse("Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here.") 

def about_view(request:HttpRequest):
    return HttpResponse("Car rental agencies primarily serve people who require a temporary vehicle, for example, those who do not own their own car, travelers who are out of town, or owners of damaged or destroyed vehicles who are awaiting repair or insurance compensation.")

def generate_pas(request:HttpRequest):
        length = 10
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return HttpResponse(password)