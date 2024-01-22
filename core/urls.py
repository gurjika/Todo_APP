from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<str:username>/tasks/', views.TasksAllView.as_view(), name='tasks'),
    path('<str:username>/tasks/<int:pk>/todos/', views.TasksView.as_view(), name='tasks-detail'),
    path('<str:username>/tasks/<int:pk>/todos/<int:todo_pk>/', views.TodosView.as_view(), name='todo-detail'),
    path('<str:username>/finished-tasks', views.FinishedTasksView.as_view(), name='finished-tasks'),
    path('add-task/', views.AddTask.as_view(), name='add-task'),
    path('update-task/<int:pk>/', views.UpdateTask.as_view(), name='update-task'),
    path('delete-task/<int:pk>/', views.DeleteTaskView.as_view(), name='delete-task'),
    path('tasks/<int:pk>/add-todo/', views.TodoAddView.as_view(), name='add-todo'),
    path('<str:username>/tasks/<int:pk>/todos/<int:todo_pk>/delete-todo/', views.DeleteTodoView.as_view(), name='delete-todo'),
    path('<str:username>/tasks/<int:pk>/todos/<int:todo_pk>/update-todo/', views.TodoUpdateView.as_view(), name='update-todo'),
]