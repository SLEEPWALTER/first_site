from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('add_course/', AddCourse.as_view(), name='add_course'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('category/<slug:cat_slug>', ShowCourses.as_view(), name='category'),
    path('course/<slug:course_slug>', show_course_post, name='course')
]