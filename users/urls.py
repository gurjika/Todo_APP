from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='sign-up'),
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('logout/', views.MyLogoutView.as_view(), name='logout'),
    path('<str:username>/',views.profile, name='profile'),

]