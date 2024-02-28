from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Task



@login_required
@require_http_methods(['DELETE'])
def delete_task(request, pk):
    Task.objects.filter(created_by=request.user).filter(pk=pk).delete()

    tasks = Task.objects.filter(created_by=request.user).filter(is_finished=False).prefetch_related('todos').all()

    return render(request, 'core/partials/tasks_all_partial.html', {'tasks': tasks, 'username': request.user.username, 'created_by': request.user})