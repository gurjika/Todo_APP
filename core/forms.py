from django import forms
from .models import Todo, Task

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['content']


class UpdateTodoForm(TodoForm):
    is_active = forms.BooleanField(label='Finished', required=False)


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']

