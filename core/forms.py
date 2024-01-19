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
    is_public = forms.BooleanField(label='Public', required=False)

    class Meta:
        model = Task
        fields = ['title', 'is_public']

class UpdateTaskForm(forms.ModelForm):
    is_finished = forms.BooleanField(label='Finished', required=False)
    is_public = forms.BooleanField(label='Public', required=False)

    class Meta:
        model = Task
        fields = ['title', 'is_finished', 'is_public']
