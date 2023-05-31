from django import forms
from .models import *


class AddCourseForm(forms.ModelForm):
    #slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Course
        fields = ['title', 'author', 'list_themes', 'about_course', 'for_whom', 'basic_requirements', 'cat']