from django.urls import include, path
from . import views


urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('tasks/', views.TasksAllView.as_view(), name='tasks'),
    path('tasks/<int:pk>/todos', views.TasksView.as_view(), name='tasks-detail'),
    path('tasks/<int:pk>/todos/<int:todo_pk>', views.TodosView.as_view(), name='todo-detail'),
    path('add-task/', views.AddTask.as_view(), name='add-task'),
    path('update-task/<int:pk>', views.UpdateTask.as_view(), name='update-task'),
    path('delete-task/<int:pk>', views.DeleteTaskView.as_view(), name='delete-task'),
    path('update-todo/tasks/<int:pk>/todos/<int:todo_pk>', views.TodoUpdateView.as_view(), name='update-todo'),
    path('tasks/<int:pk>/add-todo/', views.TodoAddView.as_view(), name='add-todo'),
    path('delete-todo/tasks/<int:pk>/todos/<int:todo_pk>', views.DeleteTodoView.as_view(), name='delete-todo'),
    path('<str:username>/tasks', views.OtherTasksView.as_view(), name='other-tasks'),
    path('<str:username>/tasks/<int:pk>', views.OtherTodosView.as_view())

]