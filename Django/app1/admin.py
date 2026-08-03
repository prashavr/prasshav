from django.contrib import admin
from .models import TodoList


class TodoListAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "status", "priority")
    search_fields = ("title", "description")
    list_filter = ("status", "priority")
    list_per_page = 5


admin.site.register(TodoList, TodoListAdmin)
