import random
import string
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def home_view(request:HttpRequest):

    return HttpResponse("Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here.")


def about_view(request:HttpRequest):

    return HttpResponse("Car rental services provide individuals and businesses with the flexibility to rent vehicles for short or long periods without the commitment of ownership. These services are ideal for travelers, those needing a temporary replacement while their car is being repaired, or businesses requiring additional transportation for employees. Most car rental companies offer a range of vehicles, from economy cars to luxury models and vans, to meet various needs and budgets. Additional options, such as insurance coverage, GPS systems, and child seats, can also be included for convenience and safety. With the rise of online booking platforms, renting a car has become a quick and hassle-free process, allowing customers to compare prices, choose their preferred vehicle, and complete reservations in just a few clicks.")



def generate_password(request:HttpResponse):
    length = 10
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return HttpResponse(f"Random password generated: {password}")

