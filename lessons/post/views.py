from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse_lazy

from .models import *
from .forms import AddCourseForm, RegisterUserForm, LoginUserForm
from django.views.generic import ListView, CreateView

menu = [
    {'title': 'Добавить курс', 'url_name': 'add_course'},
    {'title': 'Войти', 'url_name': 'login'},
    {'title': 'Регистрация', 'url_name': 'register'}
]


class HomePage(ListView):
    model = Category
    template_name = 'post/index.html'
    context_object_name = 'cats'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context


class ShowCourses(ListView):
    model = Course
    template_name = 'post/course_list.html'
    context_object_name = 'courses'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Курсы'
        return context

    def get_queryset(self):
        return Course.objects.filter(cat__slug=self.kwargs['cat_slug'])


def show_course_post(request, course_slug):
    post = Course.objects.get(slug=course_slug)
    context = {
        'title': post.title,
        'post': post
    }
    return render(request, 'post/course.html', context=context)


class AddCourse(CreateView):
    form_class = AddCourseForm
    template_name = 'post/add_course.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание курса'
        return context


# def add_course(request):
#     if request.method == 'POST':
#         form = AddCourseForm(request.POST, request.FILES)
#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.slug = form.cleaned_data['slug']
#             instance.save()
#             return redirect('home')
#     else:
#         form = AddCourseForm()
#
#     return render(request, 'post/add_course.html', {'form': form, 'title': 'Добавление курса'})


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'post/login.html'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'post/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')



def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page Not Found<h1>')
