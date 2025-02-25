from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
import string
import random
# Create your views here.
def home_view(requset:HttpRequest):
    return HttpResponse("Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here.")
def about_view(requset:HttpRequest):
    return HttpResponse("Car rental lets you use a car for a short time. ")
def password_generate_view(requset:HttpRequest):
    characters=""
    characters+=string.ascii_letters
    characters+=string.digits
    characters+=string.punctuation
    password=[]
    for i in range(10):
        password.append(random.choice(characters))

    password="".join(password)
    return HttpResponse(password)



