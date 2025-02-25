import random
import string
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here.")

def about_view(request):
    return HttpResponse("A simple paragraph about Car Rentals.")

def password_view(request):
    length = 10
    characters = string.ascii_letters + string.digits + string.punctuation  
    password = ''.join(random.choices(characters, k=length)) 

    return HttpResponse(f"Generated Password: {password}")

# Create your views here.
