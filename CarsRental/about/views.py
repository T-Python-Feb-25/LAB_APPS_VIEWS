# home/views.py

import random
import string
from django.http import HttpResponse

def home(request):
    return HttpResponse("A simple paragraph about Car Rentals.")  # Home page content

def about(request):
    return HttpResponse("Hello World, This is my new HOME for Car Rentals Website! We're excited to welcome you here.")  # About page content

def generate_password(request):
    # Define the characters to include in the password
    characters = string.ascii_letters + string.digits + string.punctuation  # letters, numbers, punctuation

    # Generate a random password of length 10
    password = ''.join(random.choice(characters) for i in range(10))

    # Return the password as a response
    return HttpResponse(password)
