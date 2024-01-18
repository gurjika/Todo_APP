from django import forms
from .models import Todo, Task

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['content']




class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']

