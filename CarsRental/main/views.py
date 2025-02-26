from django.shortcuts import render

from django.http import HttpRequest, HttpResponse
import random
import string

# Create your views here.

def home_view(request: HttpRequest):
    return HttpResponse("Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here.")


def about_view(request:HttpRequest):
    pargraph= """Car rentals provide a convenient solution for travelers and individuals in need of temporary transportation.
    With a variety of vehicles to choose from, ranging from economy cars to luxury models, rental services offer flexibility 
    to suit different budgets and preferences. Renting a car allows greater freedom to explore new places, whether on vacation 
    or for business purposes. Many rental companies also offer additional services such as GPS, insurance, and child seats, 
    making the experience hassle-free. Overall, car rentals are an efficient option for those who require a vehicle for a 
    short period without the long-term commitment of ownership."""
    return HttpResponse(pargraph)



def password_generate(request: HttpRequest):
    generate = ""
    characters = string.ascii_letters + string.digits + string.punctuation
    generate = ''.join(random.choices(characters, k=7))  

    return HttpResponse(generate)

    