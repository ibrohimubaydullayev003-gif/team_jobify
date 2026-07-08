# apps/accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib import messages
from .forms import UserRegistrationForm, UserLoginForm, ChangePasswordForm
from profiles.models import CandidateProfile, CompanyProfile
from django.contrib.auth.decorators import login_required


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
    if request.method == "POST":
        form = UserLoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:
                login(request, user)
                messages.success(request, "Muvaffaqiyatli tizimga kirdingiz.")
                return redirect("home")
            else:
                messages.error(request, "Login yoki parol noto'g'ri.")
    else:
        form = UserLoginForm()

    return render(request, "accounts/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def change_password(request):
    if request.method == "POST":
        form = ChangePasswordForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Parol muvaffaqiyatli o'zgartirildi.")
            return redirect("home")
        else:
            messages.error(request, "Parolni o'zgartirishda xatolik yuz berdi.")
    else:
        form = ChangePasswordForm(request.user)

    return render(request, "accounts/change_password.html", {"form": form})