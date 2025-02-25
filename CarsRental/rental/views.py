from django.http import HttpResponse
import random
import string


def home(request:HttpResponse):
    return HttpResponse("Hello World, This is my new HOME for Car Rentals Website | we're excited to welcome you here.")


def about(request:HttpResponse):
    return HttpResponse("A simple paragraph about Car Rentals.")


def generate_password(request):
    length = 10
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return HttpResponse("Generated Password: {password}")
