# from django.shortcuts import render

# Create your views here.
# def index(request):
#     context = {
#         "title": "Student Records",
#         "message": "This text came from the Django view.",
#     }

#     return render(request, "index.html", context)

# HOME, ABOUT US, CONTACT US, SERVICES, etc.

from multiprocessing import context

from django.http import request
from django.shortcuts import render


def index(request):
    students = [
        {
            "name": "Ram",
            "age": 16,
            "address": "Kathmandu",
        },
        {
            "name": "Sita",
            "age": 20,
            "address": "Pokhara",
        },
        {
            "name": "Hari",
            "age": 18,
            "address": "Bhaktapur",
        },
    ]

    context = {
        "title": "Student Records",
        "students": students,
    }
    return render(request, "index.html", context)

def about(request):
    context = {
        "title": "About Us",
        "description": "This is the About page of our Django project.",
    }

    return render(request, "about.html", context)