from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, View
from django.contrib.auth.views import LoginView

from core.models import Task
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# Create your views here.


class MyLoginView(LoginView):
    template_name='users/login.html'
    next_page='/'

    def get_success_url(self) -> str:
        username = self.request.user.username
        return f'/{username}'

class SignUpView(CreateView):
    form_class = RegisterForm
    template_name = 'users/signup.html'
    model = User

    def get_success_url(self) -> str:
        username = self.request.user.username
        return f'/{username}'



class MyLogoutView(View):
    def get(self, request):
        logout(request)
        return render(request, 'users/logout.html')
    


class Profile(View):
    
    def get(self, request, *args, **kwargs):
        return render(template_name='users/profile.html', request=request)
    

@login_required
def profile(request, username):

    user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            print('updated')

            return redirect('profile', username)
        
    else:
        user_form = UserUpdateForm(instance=user)
        profile_form = ProfileUpdateForm(instance=user.profile)


    profile_img = user.profile.img
    email = user.email
    task_data = None
    guest_user = False

    if user == request.user:
        task_data = Task.objects.filter(is_finished=True).filter(created_by=user).all()[:5]
    else:
        guest_user = True
        task_data = Task.objects.filter(is_finished=False) \
        .filter(created_by=user).filter(is_public=True).all()[:5]

    
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'profile_user': user,
        'task_data': task_data,
        'guest_user': guest_user,
    }

    return render(request, 'users/profile.html', context=context)


