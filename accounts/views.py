# apps/accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import UserRegistrationForm, UserLoginForm
from profiles.models import CandidateProfile, CompanyProfile


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            if user.role == 'candidate':
                CandidateProfile.objects.create(user=user)
            else:
                CompanyProfile.objects.create(user=user)
            login(request, user)
            messages.success(request, 'Muvaffaqiyatli ro‘yxatdan o‘tdingiz!')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)   # Muhim: request ni birinchi argument sifatida berish
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Login yoki parol xato!')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Parol muvaffaqiyatli o‘zgartirildi!')
            return redirect('dashboard')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})