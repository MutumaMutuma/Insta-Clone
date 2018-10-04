from django.shortcuts import render,redirect
from django.http  import HttpResponse
import datetime as dt
from django.db import models
from .models import Image,Profile
# Create your views here.

def signup(request):
    date = dt.date.today()
    
    return render(request, 'registration/homepage.html', {"date": date,})

def index(request):
    date = dt.date.today()
    photos = Image.objects.all()
    print(photos)
    profiles = Profile.objects.all()
    return render(request, 'all-posts/index.html', {"date": date, "photos":photos, "profiles":profiles,})