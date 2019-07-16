from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, Http404 ,HttpResponseRedirect
from .models import Camp,Lecture, Meeting , CampParticipant
from .forms import CampParticipantForm
from django.views.generic.edit import CreateView , UpdateView , FormMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.contrib.auth.mixins import PermissionRequiredMixin
from django import forms
from accounts.models import Profile
from django.views.generic.edit import FormView
from django.views.generic.edit import FormMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.models import User

class CampListView(ListView):
	model = Camp
	template_name = 'events/camp_list.html'
	queryset = Camp.objects.all()


class LectureListView(ListView):
	model = Lecture
	template_name = 'events/lecture_list.html'
	queryset = Lecture.objects.all()


class MeetingListView(ListView):
	model = Meeting
	template_name = 'events/meeting_list.html'
	queryset = Meeting.objects.all()


class CampDetailView(DetailView):
    model = Camp

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        prime = self.kwargs['pk']
        #In camp detail see the camp paritcipant, the set of it send by context
        context['participant_set'] = Camp.objects.get(pk=prime).campparticipant_set.all().order_by('member__member_no')
        return context

    def post(self,request,pk):
        camp_id = pk #primary key of displayed camp 
        camp=Camp.objects.get(id=int(camp_id)) #Displayed Camp object
        user= User.objects.get(id=request.user.id) #Authenticated user
        submitted_member=user.profile #Authenticated user's profile
        
        if(camp.campparticipant_set.filter(member=submitted_member)):
        #checks user is camp participant already
        #If user is camp participant already,it returns camp page and can't submit again.
            if(request.POST.get('delete')):
            #Option to delete
                a=camp.campparticipant_set.get(member=submitted_member)
                a.delete()
            return HttpResponseRedirect('/events/camps/%d/'%int(camp_id))

        if(request.POST.get('Submit')):
            #Option to submit camp
            camp.campparticipant_set.create(member=submitted_member)
        return HttpResponseRedirect('/events/camps/%d/'%int(camp_id))


class LectureDetailView(DetailView):
    model = Lecture

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        prime=self.kwargs['pk']
        #In lecture detail see the lecture paritcipant, the set of it send by context
        context['participant_set']=Lecture.objects.get(pk=prime).lectureparticipant_set.all().order_by('member__member_no')
        return context

    def post(self,request,pk):
        lecture_id = pk #primary key of displayed lecture
        lecture = Lecture.objects.get(id=int(lecture_id)) #displated lecture object
        user= request.user #Authenticated user
        submitted_member = user.profile #Authenticated user's profile
        
        if(lecture.lectureparticipant_set.filter(member=submitted_member)):
        #checks user is lecture participant already
        #If user is lecture participant already,it returns lecture page and can't submit again.
            if(request.POST.get('delete')):
            #Option to delete
                a = lecture.lectureparticipant_set.get(member=submitted_member)
                a.delete()
            return HttpResponseRedirect('/events/lectures/%d/'%int(lecture_id))
        
        if(request.POST.get('Submit')):
        #Option to submit lecture
            lecture.lectureparticipant_set.create(member=submitted_member)
        return HttpResponseRedirect('/events/lectures/%d/'%int(lecture_id))


class MeetingDetailView(DetailView):
    model = Meeting

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        prime = self.kwargs['pk']
        #In meeting detail see the meeting paritcipant, the set of it send by context
        context['participant_set']=Meeting.objects.get(pk=prime).meetingparticipant_set.all().order_by('member__member_no')
        return context

    def post(self,request,pk):
        meeting_id = pk #primary key of displayed meeetig
        meeting = Meeting.objects.get(id=int(meeting_id)) #displayed meeting object
        user = request.user #Authenticated user
        submitted_member = user.profile #Authenticated user's profile


        if(meeting.meetingparticipant_set.filter(member=submitted_member)):
        #checks user is meeting participant already
        #If user is meeting participant already,it returns meeting page and can't submit again.
            if(request.POST.get('Delete')):
            #Option to delete
                a = meeting.meetingparticipant_set.get(member=submitted_member)
                a.delete()
            return HttpResponseRedirect('/events/meetings/%d/'%int(meeting_id))
        if(request.POST.get('Submit')):
        #Option to submit meeting
            meeting.meetingparticipant_set.create(member=submitted_member)
        return HttpResponseRedirect('/events/meetings/%d/'%int(meeting_id))


class CampCreate(PermissionRequiredMixin,CreateView):
    permission_required = ('events.add_camp',)
    model = Camp
    success_url = '/events/meetings'
    fields = ['date','camp_ts','camp_ms','camp_es','camp_location']
    template_name_suffix ='_create_form'


class LectureCreate(PermissionRequiredMixin,CreateView):
    permission_required = 'events.add_lecture'
    model = Lecture
    success_url = '/events/lectures'
    fields = ['date','instructor','lecture_course']
    template_name_suffix ='_create_form'


class MeetingCreate(PermissionRequiredMixin,CreateView):
    permission_required = 'events.add_meeting'
    model = Meeting
    success_url = '/events/meetings'
    fields = ['date','location','subject']
    template_name_suffix ='_create_form'


class CampUpdate(PermissionRequiredMixin,UpdateView):
    permission_required = 'events.change_camp'
    model = Camp
    fields = ['date','camp_ts','camp_ms','camp_es','camp_location']
    template_name_suffix = '_update_form'
    success_url = '/events/camps/'


class LectureUpdate(PermissionRequiredMixin,UpdateView):
    permission_required = 'events.change_lecture'
    model = Lecture
    fields = ['lecdate','instructor','lecture_course']
    template_name_suffix = '_update_form'


class MeetingUpdate(PermissionRequiredMixin,UpdateView):
    permission_required = 'events.change_meeting'
    model = Meeting
    fields = ['date','location','subject']
    template_name_suffix = '_update_form'


