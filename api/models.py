from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    task_description = models.TextField()
    due_date = models.DateField()
    label = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
