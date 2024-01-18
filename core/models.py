from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=50)
    time_created = models.DateTimeField(default=timezone.now)
    is_finished = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('tasks-detail', kwargs={'username': self.created_by.username, 'pk': self.pk})

class Todo(models.Model):
    content = models.TextField(max_length=200)
    task = models.ForeignKey(Task, related_name='todos', on_delete=models.CASCADE)
    time_created = models.DateTimeField(default=timezone.now)
    is_finished = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('todo-detail', kwargs={'username': self.task.created_by.username, 'pk': self.task.pk, 'todo_pk': self.pk })
    
    def __str__(self):
        return self.content
