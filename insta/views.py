from django.shortcuts import render,redirect
from django.http  import HttpResponse
import datetime as dt
from django.contrib.auth.decorators import login_required
from .forms import ImageForm
from django.db import models
from .models import Image,Profile
# Create your views here.

def signup(request):
    date = dt.date.today()
    
    return render(request, 'registration/homepage.html', {"date": date,})
@login_required(login_url='/accounts/login/')
def index(request):
    date = dt.date.today()
    photos = Image.objects.all()
    print(photos)
    profiles = Profile.objects.all()
    return render(request, 'all-posts/index.html', {"date": date, "photos":photos, "profiles":profiles,})

def new_article(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.editor = current_user
            image.save()
        return redirect('NewsToday')

    else:
        form = ImageForm()
    return render(request, 'new_image.html', {"form": form})