from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Task, Todo
from django.core.paginator import Paginator
import math

@login_required
@require_http_methods(['DELETE'])
def delete_task(request, pk):
    Task.objects.filter(created_by=request.user).filter(pk=pk).delete()
    
    tasks = Task.objects.filter(created_by=request.user).filter(is_finished=False).prefetch_related('todos').all()

    paginator = Paginator(tasks, 5)  # Assuming 5 tasks per page
    page_number = len(tasks) / 5
    page_obj = paginator.get_page(page_number)


    

    context = {
        'tasks': tasks, 
        'username': request.user.username, 
        'created_by': request.user,
        'page_obj': page_obj
    }

    return render(request, 'core/partials/tasks_all_partial.html', context)


@login_required
def update_todo_status(request, todo_pk):

    print('*' * 50)

    print(todo_pk)

    print('*' * 50)
    todo = Todo.objects.get(pk=todo_pk)

    context = {}

    context['todos'] = Todo.objects.select_related('task').select_related('task__created_by'). \
    filter(task_id=todo.task.pk).all()
    context['task'] = todo.task
    

    if request.user == todo.task.created_by:
        if todo.is_finished:
            todo.is_finished = False
        else:
            todo.is_finished = True
        
        todo.save()


    return render(request, 'core/partials/generate-todos.html', context)



