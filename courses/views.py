from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, Http404 ,HttpResponseRedirect
from .models import Course
from .forms import CourseCreateForm
from django.views.generic.edit import CreateView ,UpdateView
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView , TemplateView 
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.contrib.auth.mixins import PermissionRequiredMixin

class CourseCreate(PermissionRequiredMixin,CreateView):
    permission_required = 'courses.add_course'
    model = Course
    success_url = reverse_lazy('courses:all')
    fields = ['course_code','course_name','course_content','file','photo']
    template_name_suffix = '_create_form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class CourseListView(ListView):
    model = Course
    queryset = Course.objects.all()


class CourseDetail(DetailView):
    template_name = "courses/course_detail.html"
    model = Course
    slug_field = 'course_code'


class SAT1XX(ListView):
    model = Course
    queryset = Course.objects.filter(course_code__startswith='SAT1')


class SAT2XX(ListView):
    template_name = "courses/course_list.html"
    model = Course
    queryset = Course.objects.filter(course_code__startswith='SAT2')


class SAT3XX(ListView):
    template_name = "courses/course_list.html"
    model = Course
    queryset = Course.objects.filter(course_code__startswith='SAT3')


class SAT4XX(ListView):
    template_name = "courses/course_list.html"
    model = Course
    queryset = Course.objects.filter(course_code__startswith='SAT4')


class CourseUpdate(PermissionRequiredMixin,UpdateView):
    permission_required = 'courses.change_course'
    model = Course
    fields = ['course_code','course_name','course_content','file','photo']
    slug_field = 'course_code'
    template_name = 'courses/course_update_form.html'
    success_url = reverse_lazy('courses:all')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
