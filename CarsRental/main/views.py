import string

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random
from string import digits, ascii_lowercase, ascii_uppercase

# Create your views here.


def home_view(request: HttpRequest):

    return HttpResponse("Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here."
                        "")


def about_view(request: HttpRequest):

    return HttpResponse("<h3>About Us</h3> "
                        "</p>Car Hire Hobart: SafeDrive Car Rentals — Your Trusted Partner for Hassle-Free Car Rentals"
                        "Dedicated to giving you a fantastic rental experience, SafeDrive Car Rentals is a proudly "
                        "Tasmanian-owned and functioned company. We pledge to provide customers with a large selection "
                        "of perfect cars, outstanding customer support, and reasonable rates to ensure that their trip "
                        "through Tasmania is as smooth and pleasurable as possible.</p> SafeDrive Car Rentals is a family "
                        "owned company, established with the goal of offering a customised and client focused car rental "
                        "experience. We understand that renting a car can be a challenging task, so we work effortlessly "
                        "to make it as simple and clear as we can for our valued customers.</p>At SafeDrive Car Rentals, "
                        "we’re dedicated to consistently going above for our clients by offering more promising customer "
                        "service. Our team of helpful and friendly employees is always happy to help you with your rental "
                        "needs. From helping you choose the right vehicle to giving you advice and directions around the "
                        "area.</p>")


def password_generate_view(request: HttpRequest):

    random_char = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    random_pass = ''.join(random.choices(random_char, k=10))
    return HttpResponse(f"Your random password is: {random_pass}")

