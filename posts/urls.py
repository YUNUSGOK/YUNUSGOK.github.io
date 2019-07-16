from django.urls import path ,include

from . import views


urlpatterns = [
    
    path('', views.HomeView.as_view() , name='home'),
    path('about/' , views.AboutView.as_view() , name='about'), 
    path('announcements/' , views.AnnouncementList.as_view() , name='announcements'), 
    path('announcements/<pk>/' , views.AnnouncementDetail.as_view() , name='announcement_detail')
]