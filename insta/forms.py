from django import forms
from .models import Image,Profile,Comments
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['likes','profile','posted_time','profile','user']

class SignupForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name','last_name','bio','profile_pic'] 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['image','user']