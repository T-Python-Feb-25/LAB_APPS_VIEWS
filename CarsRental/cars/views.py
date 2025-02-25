from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
import random
import string
# Create your views here.

def page1 (request:HttpRequest):
    return HttpResponse("Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here.")

def page2(request:HttpRequest):
    return HttpResponse("A simple paragraph about Car Rentals.")

def bouns(request:HttpRequest):
    length = 10 
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return HttpResponse((f"the random password is : {password}"))