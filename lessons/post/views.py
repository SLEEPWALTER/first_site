from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse_lazy

from .models import *
from .forms import AddCourseForm
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


def login(request):
    return HttpResponse('<h1>login page</h1>')


def register(request):
    return HttpResponse('<h1>register page</h1>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page Not Found<h1>')
