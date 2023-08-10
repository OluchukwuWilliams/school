import uuid 
import json 
import requests
from django.shortcuts import render, get_object_or_404, redirect 
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from home.models import *
from django.contrib.auth import login, logout, authenticate 
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from . models import * 
from . forms import * 
from django.conf import settings
from userprofile.models import *  
from userprofile.forms import * 
from django.core.mail import send_mail
from django.db.models import Q 
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return render(request, 'index.html')

def quiz(request):
    quiz = Quiz.objects.order_by('id').all()

    context = {
        'quiz': quiz,
    }
    return render(request, 'quiz.html', context)


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"message sent successfully")
            return redirect('index')
        else:
            messages.error(request, form.errors)
            return redirect('index')
    return redirect('index')

def economics(request):
    return render(request, 'Economics.html')

def english(request):
    return render(request, 'English.html')



def biology(request):
    return render(request, 'Biology.html')


def mathematics(request):
    # mathematics = Mathematics.objects.order_by('id').all()

    context = {
        'mathematics': mathematics
    }
    return render(request, 'Mathematics.html', context)


def mathematics2(request):
    return render(request, 'Mathematics2.html')


@login_required(login_url='signin')
def profile(request):
    profile = Profile.objects.get(user__username=request.user.username)

    context = {
        'profile': profile,
    }

    return render(request, 'profile.html', context)
    

@login_required(login_url='signin')
def profile_update(request):
    profile = Profile.objects.get(user__username=request.user.username)
    update = ProfileUpdate(instance=request.user.profile)
    if request.method == 'POST':
        update = ProfileUpdate(request.POST, request.FILES, instance=request.user.profile)
        if update.is_valid():
            update.save()
            messages.success(request, "User profile updated successfully")
            return redirect('profile')
        else:
            messages.error(request, update.errors)
            return redirect('profile_update')
    context = {
        'profile': profile,
        'update': update,
    }
    return render(request, 'profile_update.html', context)

def signin(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password'] 
        user = authenticate(username = username, password = password) 
        if user is not None:
            login(request, user)
            messages.success(request, "sign in successful")
            return redirect('profile') 
        else:
            messages.error(request, 'invalid username or password')
            return redirect('signin')
        
    return render(request, 'signin.html')

@login_required(login_url='signin')
def signout(request):
    logout(request)
    return redirect('index')


def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        pix = request.POST['pix']
        address = request.POST['address']
        dob = request.POST['dob']
        nationality = request.POST['nationality']
        gender = request.POST['gender']
        state = request.POST['state']
        phone = request.POST['phone']
        form = SignupForm(request.POST)
        if form.is_valid():
            newuser = form.save()
            newprofile = Profile(user=newuser)
            newprofile.username = newuser.username
            newprofile.firstname = newuser.first_name
            newprofile.lastname = newuser.last_name
            newprofile.email = newuser.email 
            newprofile.pix = pix 
            newprofile.address = address 
            newprofile.dob = dob 
            newprofile.nationality = nationality 
            newprofile.gender = gender 
            newprofile.state = state 
            newprofile.phone = phone 
            newprofile.save()
            login(request, newuser)
            messages.success(request, f"welcome {newuser.username}!, Signup successful")
            send_mail (
                "Thank You",
                "we got your message... and it will be attended to shortly",
                {newuser.email},
                settings.EMAIL_HOST_USER,
                fail_silently=False,
            )
            return redirect('signin')
        else:
            messages.error(request, form.errors)
            return redirect('signup')
        
    return render(request, 'signup.html')
            
def password(request):
    profile = Profile.objects.get(user__username=request.user.username)
    form = PasswordChangeForm(request.user)
    if request.method =='POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'password change successfully!')
            return redirect('profile')
        else:
            messages.error(request, form.errors)
            return redirect('password')
    
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'password.html', context)
    
