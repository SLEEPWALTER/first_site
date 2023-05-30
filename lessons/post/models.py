from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    photo = models.ImageField(upload_to='photos/', verbose_name='Фотография')

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Course(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название курса')
    author = models.CharField(max_length=255, verbose_name='Автор')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    list_themes = models.TextField(verbose_name='Список тем')
    about_course = models.TextField(verbose_name='О курсе')
    for_whom = models.TextField(verbose_name='Для кого')
    basic_requirements = models.TextField(verbose_name='Начальные требования')
    course_program = models.TextField(verbose_name='Программа курса')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('category', kwargs={'course_slug': self.slug})

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'