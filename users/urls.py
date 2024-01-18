from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='sign-up'),
    path('login/', auth_views.
         LoginView.as_view(template_name='users/login.html', next_page='/home'), name='login'),
    path('logout/', views.MyLogoutView.as_view(), name='logout')
]