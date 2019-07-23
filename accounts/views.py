from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User ,Group
from django.shortcuts import render, HttpResponseRedirect, redirect
from django import forms
from django.contrib.auth.decorators import login_required
from .models import Profile ,SignUpRequest
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied
from django.views.generic.edit import FormView
from .forms import UserForm, ProfileForm
from django.views.generic import ListView 
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import CreateView , UpdateView , FormMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from datetime import datetime
from .forms import SignupRequestCreateForm


class ProfileListView(ListView):
    model = Profile
    template_name = 'accounts/member_list.html'
    queryset = Profile.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        n=int(self.kwargs['n']) #dividing member list to 100 member at a page       
        context['member_set'] =  queryset = Profile.objects.all()[(n-1)*100:n*100]
        context['n']=n
        return context


class BoardMemberListView(ListView):#Groups with autherized member
    model = Group #Django default auth models
    template_name = 'accounts/board_member_list.html'
    queryset = [
                Group.objects.get(name='Yürütme Kurulu'),
                Group.objects.get(name='Denetleme Kurulu'),
                Group.objects.get(name='Teknik Kurul')
                ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['yk'] = Group.objects.get(name='Yürütme Kurulu').user_set.all()
        context['dk'] = Group.objects.get(name='Denetleme Kurulu').user_set.all()
        context['tk'] = Group.objects.get(name='Teknik Kurul').user_set.all()
        return context


class SignUpRequestCreate(generic.CreateView):
    form_class = SignupRequestCreateForm #from forms.py 
    model = SignUpRequest 
    success_url = reverse_lazy('home') #return to home page


class SignUpRequestListView(ListView):
    #SignUpRequest list for authorized users to approve or dissapprove 
    model = SignUpRequest
    template_name = '/accounts/request_list.html'
    queryset = SignUpRequest.objects.all()

    def post(self,request):#Post data can be used from this func
        request_id = request.POST.get('request_id')#id to reach object
        signup_request = SignUpRequest.objects.get(id=int(request_id))#request object

        if(request.POST.get('delete')):#disapprove option 
            signup_request.delete() #delete request
            return HttpResponseRedirect('/accounts/requests')

        if(request.POST.get('Submit')):#approve option
            #checks username for already existing username
            if(User.objects.filter(username=signup_request.username)):
                #if username exists it returns to list again
                return HttpResponseRedirect('/accounts/requests')
            if(signup_request.password1 != signup_request.password2):
                #confirms password
                #If passwords don't match it returns to list again
                return HttpResponseRedirect('/accounts/requests')
            #User creation from given informations in request
            user=User(
                username=signup_request.username,
                first_name=signup_request.first_name,
                last_name=signup_request.last_name,
                email=signup_request.email,
                id=signup_request.member_no,
                )
            
            user.set_password(signup_request.password1)#for encrypted password
            user.save()
            #request contains member_no from profile model 
            user.profile.member_no = signup_request.member_no 
            user.profile.save()

            signup_request.delete() #when user creation is done, deleting the request
            return HttpResponseRedirect(reverse_lazy("requests"))


class ProfileUpdate(DetailView):
    model = User #Profile can be reached from User model
    template_name = 'profile_update_form.html'
    def get_context_data(self, **kwargs): #to send extra info to page, overriding the orginal function 
        context = super().get_context_data(**kwargs) #inherits from original function, and its context
        context['now'] = timezone.now() #current time
        user_id = self.kwargs['pk'] #user id from url primary key(pk)
        user = User.objects.get(id=user_id) #User object of registered user
        x=[]
        y=[]
        #types and levels are array with has tuple elements[('type1','type1'),('type2','type2')].
        #Iteration to get first elemts of tuples.
        for i in Profile.types:
            x.append(i[0])
        for i in Profile.levels:
            y.append(i[0])

        context['blood_types'] = x 
        context['levels'] = y
        #html date input excepts YYYY-MM-DD format, because of that strftime will 
        #convert datefield to proper format 
        date = user.profile.birth_date 
        context['user_date'] = date.strftime('%Y-%m-%d')
        return context

    def post(self,request,pk):
        user_id = int(pk)
        user = User.objects.get(id=user_id)
        profile=user.profile
        if(request.POST.get('save')):#Saves button click check to update profile 
            user.email = request.POST.get('email',user.email)
            profile.phone = request.POST.get('phone',profile.phone)
            profile.birth_date = request.POST.get('birth_date',profile.birth_date)
            profile.date = request.POST.get('date', profile.date)
            profile.dive_count = request.POST.get('count', profile.dive_count)
            profile.dive_level = request.POST.get('level', profile.dive_level)
            profile.department = request.POST.get('department' , profile.department )
            profile.blood_type = request.POST.get('blood_types' , profile.blood_type ) 
            if(request.FILES.get('pp_image')):#checks whether there is an image input to change pp
                profile.photo = request.FILES['pp_image']
            profile.save()
            user.save()

        return HttpResponseRedirect(reverse_lazy('profile_view'))#when profile is updated, returns profile detail page 
        


class ProfileDetailView(DetailView):  #Profile details for only authenticated users to acces other users' informations
    model = User
    template_name = 'profile_detail.html'
        

def profile_view(request):#Authenticated user's personal profile detail page
    user = request.user
    
    taken_courses= user.profile.takencourse_set.all()#courses user took

    #events user participated 
    camps = user.profile.campparticipant_set.all() 
    lectures = user.profile.lectureparticipant_set.all()
    meetings = user.profile.meetingparticipant_set.all() 

    context= {'user':user , 'taken_courses' :taken_courses , 
        'camps':camps, 'lectures': lectures,'meetings':meetings }
    return render(request, 'accounts/profile_detail.html', 
        context) 

