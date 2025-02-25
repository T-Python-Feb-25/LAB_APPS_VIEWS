from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
# Create your views here.
import random
import string

def home_view(request:HttpRequest):

    return HttpResponse("Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here.")


def about_view(request:HttpRequest):

    return HttpResponse('''Car rental agencies primarily serve people who require a temporary vehicle, for example, those who do not own their own car,
travelers who are out of town, or owners of damaged or destroyed vehicles who are awaiting repair or insurance compensation.
Car rental agencies may also serve the self-moving industry needs, by renting vans or trucks, and in certain markets,
other types of vehicles such as motorcycles or scooters may also be offered.''')

def password_generator_view(request:HttpRequest):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(all_characters, k=10))
    return HttpResponse(f"This is a generated password: {password}")

