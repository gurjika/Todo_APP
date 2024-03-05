from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Task
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