from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CandidateProfileForm, CompanyProfileForm

@login_required
def profile_view(request):
    user = request.user
    if user.role == 'candidate':
        profile = user.candidate_profile
        form = CandidateProfileForm(instance=profile)
    else:
        profile = user.company_profile
        form = CompanyProfileForm(instance=profile)
    return render(request, 'profiles/profile.html', {'form': form, 'profile': profile})

@login_required
def profile_edit(request):
    user = request.user
    if user.role == 'candidate':
        profile = user.candidate_profile
        form_class = CandidateProfileForm
    else:
        profile = user.company_profile
        form_class = CompanyProfileForm
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil yangilandi!')
            return redirect('profile')
    else:
        form = form_class(instance=profile)
    return render(request, 'profiles/profile_edit.html', {'form': form})


