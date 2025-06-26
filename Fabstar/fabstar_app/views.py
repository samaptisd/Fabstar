from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import UserForm, ProfileForm
from .models import Profile

from django.contrib.auth.views import (
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,
    PasswordResetCompleteView, LoginView, LogoutView
)



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to home after successful login
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {'error': 'Invalid login credentials'})
    return render(request, 'login.html')

@login_required(login_url='/accounts/login/?next=/')
def home(request):
    return render(request, 'fabstar_app/home.html')

@login_required(login_url='/accounts/login/?next=/')
def profile(request):
    user = request.user
    Profile.objects.get_or_create(user=user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'fabstar_app/profile.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required(login_url='/accounts/login/?next=/')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'fabstar_app/change_password.html', {'form': form})

# Other views (they are fine):
def aludecor_technical_manual(request):
    return render(request, 'fabstar_app/aludecor_technical_manual.html')

def aludecor_calculator(request):
    return render(request, 'fabstar_app/aludecor_calculator.html')

def aludecor_design_assist(request):
    return render(request, 'fabstar_app/aludecor_design_assist.html')

def fabstar_app(request):
    return render(request, 'fabstar_app/fabstar_app.html')

def connect_with_dr_aludecor(request):
    return render(request, 'fabstar_app/connect_with_dr_aludecor.html')

def aludecor_flipbook(request):
    return render(request, 'fabstar_app/aludecor_flipbook.html')

@login_required(login_url='/accounts/login/?next=/')
def password_changed(request):
    return render(request, 'fabstar_app/password_changed.html')

# def custom_logout(request):
#     return render(request, 'registration/logged_out.html')

def custom_logout(request):
    if request.method == 'POST':
        LogoutView(request)
        
        return redirect('login')
    else:
        return redirect('login') 

def book_view(request):
    pages = list(range(1, 122)) 
    return render(request, 'fabstar_app/aludecor_technical_manual.html', {'pages': pages})

import logging

user_logger = logging.getLogger('user_activity')

def some_view(request):
    if request.user.is_authenticated:
        user_logger.info(f"{request.user.username} accessed {request.path}")
    ...

