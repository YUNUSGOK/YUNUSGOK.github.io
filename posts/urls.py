from django.urls import path ,include
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    
    path('home/', views.HomeView.as_view() , name='home'),
    path('about/' , views.AboutView.as_view() , name='about'), 
    path('announcements/' , views.AnnouncementList.as_view() , name='announcements'), 
    path('announcements/<pk>/' , views.AnnouncementDetail.as_view() , name='announcement_detail'),
    path('',TemplateView.as_view(template_name='posts/welcome.html'),name='welcome')
]