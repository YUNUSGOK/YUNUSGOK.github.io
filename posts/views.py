from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import About , Announcement ,Photo
from django.views.generic.detail import DetailView
from accounts.models import SignUpRequest
from django.contrib.auth.models import User ,Group
import random
from django.utils import timezone


class HomeView(TemplateView):
    template_name = "posts/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['announcement_list']=Announcement.objects.all()[::-1][:4] #last 4 announcement to display
        context['photos']=Photo.objects.order_by('?')[:3] #random 3 pohoto to display
        context['groups']= Group.objects.all()
        return context


class AboutView(TemplateView):
    template_name  = 'posts/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_list'] = About.objects.all() # Odd entrys which display photo left
        context['about_list1'] = About.objects.all()[::2] # Even entries which display photo right
        return context


class AnnouncementList(ListView):
    model = Announcement


class AnnouncementDetail(DetailView):
    model = Announcement