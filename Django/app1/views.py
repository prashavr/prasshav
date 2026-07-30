from django.shortcuts import render
from .models import TodoList

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

def contact(request):
    context = {
        "title": "Contact Us",
        "email": "hello@example.com",
        "phone": "+977 9800000000",
    }

    return render(request, "contact.html", context)

def todo_list(request):
    todos = TodoList.objects.all().order_by("id")

    context = {
        "title": "Todo List",
        "todos": todos,
    }

    return render(request, "todos.html", context)