from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('add_course/', add_course, name='add_course'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('category/<slug:cat_slug>', ShowCourses.as_view(), name='category'),
    path('course/<slug:course_slug>', show_course_post, name='course')
]