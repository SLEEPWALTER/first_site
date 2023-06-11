from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *


class AddCourseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Course
        fields = ['title', 'author', 'list_themes', 'about_course', 'for_whom', 'basic_requirements', 'cat']


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login')
    password1 = forms.CharField(label='Password')
    password2 = forms.CharField(label='Repeate password')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='login')
    password = forms.CharField(label='password')




