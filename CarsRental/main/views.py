from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random
import string
# Create your views here.

# Main
def main_view(request:HttpRequest):
  content = "Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here."
  return HttpResponse(content)

# About
def about_view(request:HttpRequest):
  content = "Car rentals offer a convenient way to use a vehicle temporarily. They provide various car options for travel, business, or daily needs. Rental companies require a valid license and a deposit, with options like insurance and flexible rental periods."
  return HttpResponse(content)

# Bonus
def generate_password(request:HttpRequest):
  # Setting up the digits, letters, special chars
  letters = string.ascii_letters
  digits = string.digits
  special_chars = string.punctuation
  # Concat them
  all = letters + digits + special_chars
  # Generate password
  password = "".join(random.choices(all, k=10))
  return HttpResponse(password)

