from django.urls import path

from . import views


app_name = 'courses'
urlpatterns = [
    path('', views.CourseListView.as_view(), name='all'),
    path('SAT1XX/',views.SAT1XX.as_view(), name='sat1xx'),
    path('SAT2XX/',views.SAT2XX.as_view(), name='sat2xx'),
    path('SAT3XX/',views.SAT3XX.as_view(), name='sat3xx'),
    path('SAT4XX/',views.SAT4XX.as_view(), name='sat4xx'),
    path('create/',views.CourseCreate.as_view(),name='create_course'),
    path('<slug:slug>/',views.CourseDetail.as_view(), name='detail'),
    path('<slug:slug>/edit',views.CourseUpdate.as_view(),name='edit_course'),



]