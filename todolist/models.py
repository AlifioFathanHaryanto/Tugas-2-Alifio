from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length=255)
    description = models.TextField()