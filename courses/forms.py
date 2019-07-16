from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from courses.models import Course


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('course_code', 'course_name','course_content','last_update')