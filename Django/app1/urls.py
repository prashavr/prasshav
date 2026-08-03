from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("todos/", views.todo_list, name="todos"),
    path("todos/create/", views.create_task, name="create_task"),
    path(
    "todos/<int:todo_id>/edit/",
    views.edit_task,
    name="edit_task",
),
    path(
    "todos/<int:todo_id>/complete/",
    views.complete_task,
    name="complete_task",
),
    path(
    "todos/<int:todo_id>/delete/",
    views.delete_task,
    name="delete_task",
),
]