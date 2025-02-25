from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random
import string
from django.http import JsonResponse
# Create your views here.

def page_view(request : HttpRequest):
    content = "content to be sent"
    return HttpResponse(content)

def page_main(request : HttpRequest):
    main = "Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here."
    return HttpResponse(main)

def page_about(request : HttpRequest):
    about = "Car rentals are subject to many conditions which vary from one country to another and from one company to another. Generally the vehicle must be returned in the same condition it was rented in, and often must not exceed mileage restrictions, otherwise, extra fees may be incurred"
    return HttpResponse(about)


def page_bouns(request):
    length = 10  
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))  
    return JsonResponse({"password": password})
