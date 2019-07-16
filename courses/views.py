from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, Http404 ,HttpResponseRedirect
from .models import Course
from .forms import CourseCreateForm
from django.views.generic.edit import CreateView ,UpdateView
from django.urls import reverse_lazy
from django.views.generic import ListView , TemplateView 
from django.views.generic.detail import DetailView


class CourseCreate(CreateView):
    model = Course
    success_url = reverse_lazy('home')
    fields = ['course_code','course_name','course_content','last_update']
    template_name_suffix = '_create_form'


class CourseListView(ListView):
    model = Course
    queryset = Course.objects.all()


class CourseDetail(DetailView):
    template_name = "courses/detail.html"
    model = Course
    slug_field = 'course_code'


class SAT1XX(ListView):
    model = Course
    queryset = Course.objects.filter(course_code__startswith='SAT1')


class SAT2XX(ListView):
    model = Course
    queryset = Course.objects.filter(course_code__startswith='SAT2')


class SAT3XX(ListView):
    model = Course
    queryset = Course.objects.filter(course_code__startswith='SAT3')


class SAT4XX(ListView):
    model = Course
    queryset = Course.objects.filter(course_code__startswith='SAT4')


class CourseUpdate(UpdateView):
    model = Course
    fields = ['course_code','course_name','course_content','last_update']
    slug_field = 'course_code'
    template_name = 'courses/course_update_form.html'


