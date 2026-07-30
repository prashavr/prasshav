from django.db import models


class TodoList(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, default="medium")

    def __str__(self):
        return self.title