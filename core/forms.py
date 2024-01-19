from django import forms
from .models import Todo, Task

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['content']


class UpdateTodoForm(forms.ModelForm):
    is_finished = forms.BooleanField(label='Finished', required=False)
    class Meta:
        model = Todo
        fields = ['content', 'is_finished']
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']

class UpdateTaskForm(forms.ModelForm):
    is_finished = forms.BooleanField(label='Finished', required=False)

    class Meta:
        model = Task
        fields = ['title', 'is_finished']
