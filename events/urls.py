from django.urls import path

from . import views


app_name = 'events'
urlpatterns = [
    #<---------------------Event List Pages------------------------------------->
    path('camps/' ,  views.CampListView.as_view() ,  name='camps') ,
    path('lectures/' ,  views.LectureListView.as_view() ,  name='lectures') , 
    path('meetings/' ,  views.MeetingListView.as_view() ,  name='meetings') , 

    #<---------------------Event Creation Pages------------------------------------->
    path('camps/create/' , views.CampCreate.as_view() ,  name='create_camp') , 
    path('lectures/create/' , views.LectureCreate.as_view() ,  name='create_lecture') , 
    path('meetings/create/' , views.MeetingCreate.as_view() ,  name='create_meeting') , 

    #<---------------------Event Detail Pages------------------------------------->
    path('camps/<pk>/' ,  views.CampDetailView.as_view() ,  name='camp-detail') , 
    path('lectures/<pk>/' ,  views.LectureDetailView.as_view() ,  name='lecture-detail') , 
	path('meetings/<pk>/' ,  views.MeetingDetailView.as_view() ,  name='meeting-detail') , 

    #<---------------------Event Update Pages------------------------------------->
    path('camps/<pk>/update' , views.CampUpdate.as_view() , name='update_camp') , 
    path('lectures/<pk>/update' , views.LectureUpdate.as_view() , name='update_lecture') , 
    path('meetings/<pk>/update' , views.MeetingUpdate.as_view() , name='update_meeting') , 



]