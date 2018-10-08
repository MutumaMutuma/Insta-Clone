from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse
import datetime as dt
from .email import send_welcome_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ImageForm, SignupForm, CommentForm
from django.db import models
from .models import Image,Profile
# Create your views here.

def signup(request):
    date = dt.date.today()
    
    return render(request, 'registration/homepage.html', {"date": date,})



@login_required(login_url='/home')
def index(request):
    date = dt.date.today()
    photos = Image.objects.all()
    # print(photos)
    profiles = Profile.objects.all()
    # print(profiles)
    form = CommentForm()

    return render(request, 'all-posts/index.html', {"date": date, "photos":photos, "profiles":profiles, "form":form})

def new_image(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.profile = profile
            image.save()
        return redirect('index')

    else:
        form = ImageForm()
    return render(request, 'new_image.html', {"form": form})

def profile(request):
    date = dt.date.today()
    current_user = request.user
    profile = Profile.objects.get(user=current_user.id)
    print(profile.profile_pic)
    
    if request.method == 'POST':
        signup_form = SignupForm(request.POST, request.FILES,instance=request.user.profile) 
        if signup_form.is_valid():
           signup_form.save()
    else:        
        signup_form =SignupForm() 
    
    return render(request, 'registration/profile.html', {"date": date, "form":signup_form,"profile":profile})

@login_required(login_url='/accounts/login/')
def comment(request,image_id):
    #Getting comment form data
    if request.method == 'POST':
        image = get_object_or_404(Image, pk = image_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.image = image
            comment.save()
    return redirect('index')
    

@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_users = User.objects.filter(username=search_term)
        message = f"{search_term}"
        profiles=  Profile.objects.all( )
        
        return render(request, 'all-posts/search.html',{"message":message,"users": searched_users,'profiles':profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-posts/search.html',{"message":message})
