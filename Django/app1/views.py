from django.shortcuts import get_object_or_404, redirect, render
from .models import TodoList
from django.views.decorators.http import require_POST

def index(request):
    students = [
        {
            "name": "Prashav",
            "age": 23,
            "address": "Lalitpur",
        },
        {
            "name": "Sashwat",
            "age": 21,
            "address": "Lalitpur",
        },
        {
            "name": "Bhumika",
            "age": 22,
            "address": "Kathmandu",
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

def create_task(request):
    error = None

    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        description = request.POST.get("description", "").strip()

        if not title or not description:
            error = "Title and description are required."
        else:
            TodoList.objects.create(
                title=title,
                description=description,
            )
            return redirect("todos")

    return render(request, "create.html", {"error": error})

def edit_task(request, todo_id):
    todo = get_object_or_404(TodoList, pk=todo_id)
    error = None

    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        description = request.POST.get("description", "").strip()

        if not title or not description:
            error = "Title and description are required."
        else:
            todo.title = title
            todo.description = description
            todo.save()

            return redirect("todos")

    context = {
        "todo": todo,
        "error": error,
    }

    return render(request, "edit.html", context)

@require_POST
def complete_task(request, todo_id):
    todo = get_object_or_404(TodoList, pk=todo_id)

    todo.status = True
    todo.save(update_fields=["status"])

    return redirect("todos")

@require_POST
def delete_task(request, todo_id):
    todo = get_object_or_404(TodoList, pk=todo_id)
    todo.delete()

    return redirect("todos")