from django import forms
from django.utils.text import slugify
from .models import *


class AddCourseForm(forms.ModelForm):
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')

        if title:
            slug = slugify(title)
            cleaned_data['slug'] = slug

        return cleaned_data

    class Meta:
        model = Course
        fields = ['title', 'author', 'list_themes', 'about_course', 'for_whom', 'basic_requirements', 'cat']