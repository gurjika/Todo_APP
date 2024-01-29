from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea, required=False)
    img = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'img-class'}))
    class Meta:
        model = Profile
        fields = ['img', 'bio']