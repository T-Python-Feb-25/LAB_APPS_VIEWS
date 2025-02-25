from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import string
import random


# Create your views here.
def home_view(request:HttpRequest):
  return HttpResponse("Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here")

def about_view(request:HttpRequest):
  return HttpResponse("A simple paragraph about Car Rentals. ")

def password_generate(request:HttpRequest):
  length = 10
  characters = string.ascii_letters + string.digits + string.punctuation
  password = ''.join(random.choice(characters) for i in range(length))
  return HttpResponse(password)



