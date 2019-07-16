# accounts/urls.py
from django.urls import path ,include

from . import views



urlpatterns = [

    #includes login and password operations given by django
    path('', include('django.contrib.auth.urls')),

    #SignUpRequest creation form to send admin to register
    path('signup/', views.SignUpRequestCreate.as_view(), name='signup'),

    #SignUpRequest list for authorized users to approve or dissapprove 
    path('requests/',views.SignUpRequestListView.as_view(),name='requests'),

    #Profile  list for both authenticated and unauthenticated users
    path('members/list<n>/',views.ProfileListView.as_view(),name='members'),

    #Profile details for only authenticated users to acces other users' informations
    path('members/<pk>/',views.ProfileDetailView.as_view(),name='memberdetail'),

    #Authenticated user's personal profile edit page
    path('profile/<pk>/edit/', views.ProfileUpdate.as_view(), name='edit_profile'),

    #Authenticated user's personal profile detail page
    path('profile/',views.profile_view,name='profile_view'),

    #List of authorized members to contact them
    path('boardmembers/',views.BoardMemberListView.as_view(),name='boardmembers'),

    path('boards/<pk>/',views.GroupDetail.as_view(),name='boards')
    

]