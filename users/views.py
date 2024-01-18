from django.shortcuts import render
from django.views.generic import CreateView, View
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import logout
# Create your views here.



class SignUpView(CreateView):
    form_class = RegisterForm
    template_name = 'users/signup.html'
    model = User

    success_url = '/home'



class MyLogoutView(View):
    def get(self, request):
        logout(request)
        return render(request, 'users/logout.html')
    


class Profile(View):
    
    def get(self, request, *args, **kwargs):
        return render(template_name='users/profile.html', request=request)