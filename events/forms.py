from django import forms
from django.contrib.auth.models import User
from .models import Camp, Lecture ,Meeting ,CampParticipant

class CampParticipantForm(forms.ModelForm):
	class Meta:
		model = CampParticipant
		fields = ['event','member']
