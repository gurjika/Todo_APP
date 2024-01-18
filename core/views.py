from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, TemplateView, DetailView, View, CreateView, UpdateView, DeleteView
from .models import Task, Todo
from .forms import TaskForm, TodoForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.


class TodoObjectMixin:
    def get_object(self):
        task_id = self.kwargs.get('pk')
        todo_id = self.kwargs.get('todo_pk')
    
        
        obj = get_object_or_404(Todo.objects.select_related('task__created_by'), task__id=task_id, pk=todo_id)
        return obj

    def test_func(self):
        todo = self.get_object()
        if self.request.user == todo.task.created_by:
            return True
        return False
    
     
class TaskTestUserMixin:
        def test_func(self):
            task = get_object_or_404(Task, pk=self.kwargs['pk'])

            if self.request.user == task.created_by:
                return True
            return False


    
class QueryTasksByUsername:
    def get_queryset(self):
        username = self.kwargs['username']
        user = get_object_or_404(User, username=username)

        queryset = Task.objects.filter(created_by=user)
        if self.request.user == user:
            return queryset
        else:
            queryset = queryset.filter(is_public=True)
            return queryset
        
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['username'] = self.kwargs['username']
        return context

  

    

class TasksView(QueryTasksByUsername, LoginRequiredMixin, ListView):
    template_name = 'core/tasks_detail.html'
    context_object_name = 'tasks'

    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['todos'] = Todo.objects.select_related('task').select_related('task__created_by').filter(task_id=self.kwargs['pk']).all()
        return context
    
 
    
    

class TasksAllView(QueryTasksByUsername, LoginRequiredMixin, ListView):
    template_name = 'core/tasks_all.html'
    context_object_name = 'tasks'

   



class TodosView(TodoObjectMixin, LoginRequiredMixin, UserPassesTestMixin, DetailView):
    template_name = 'core/todo_detail.html'
    context_object_name = 'todo'

  
   

    
    

class HomeView(TemplateView):
    template_name = 'core/home.html'


class AddTask(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'core/add_task.html'


    def form_valid(self, form: BaseModelForm):
        author = self.request.user
        form.instance.created_by = author
        return super().form_valid(form)    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Task'
        return context


class UpdateTask(TaskTestUserMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'core/add_task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Task'
        return context
    
   
class TodoUpdateView(TodoObjectMixin, UserPassesTestMixin, UpdateView):
    template_name = 'core/todo_add.html'
    model = Todo
    form_class = TodoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Todo'
        return context
    

class TodoAddView(TaskTestUserMixin, LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name = 'core/todo_add.html'
    model = Todo
    form_class = TodoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Todo'
        return context
    
    def form_valid(self, form: BaseModelForm):
        task = Task.objects.get(pk=self.kwargs['pk'])
        form.instance.task = task
        return super().form_valid(form)
    

    


class DeleteTodoView(TodoObjectMixin, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Todo
    
    def get_success_url(self):
        pk = self.kwargs['pk']
        return f'/tasks/{pk}/todos'
    
    
class DeleteTaskView(TaskTestUserMixin, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task

    def get_success_url(self):
        return f'/tasks'
    


        
    