from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import Profile ,SignUpRequest


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('member_no', 'phone','dive_count','birth_date','blood_type','photo','dive_level','department')


class SignupRequestCreateForm(forms.ModelForm):
    class Meta:
        model = SignUpRequest
        fields = ['username','first_name', 'last_name', 'member_no','email', 'password1','password2']
        widgets = {
            'password1': forms.PasswordInput(),'password2': forms.PasswordInput()
        }