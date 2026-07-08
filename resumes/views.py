from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Resume
from .forms import ResumeForm

@login_required
def resume_list(request):
    resumes = request.user.resumes.all()
    return render(request, 'resumes/resume_list.html', {'resumes': resumes})

@login_required
def resume_create(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.candidate = request.user   
            resume.save()
            messages.success(request, 'Rezyume yaratildi!')
            return redirect('resumes:list')
    else:
        form = ResumeForm()
    return render(request, 'resumes/resume_form.html', {'form': form, 'action': 'Yaratish'})

@login_required
def resume_update(request, pk):
    resume = get_object_or_404(Resume, pk=pk, candidate=request.user)
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES, instance=resume)
        if form.is_valid():
            form.save()
            messages.success(request, 'Rezyume yangilandi!')
            return redirect('resume_list')
    else:
        form = ResumeForm(instance=resume)
    return render(request, 'resumes/resume_form.html', {'form': form, 'action': 'Yangilash'})

@login_required
def resume_delete(request, pk):
    try:
        resume = Resume.objects.get(pk=pk, candidate=request.user)
    except Resume.DoesNotExist:
        messages.error(request, 'Rezyume topilmadi yoki sizga tegishli emas.')
        return redirect('resumes:list')
    
    if request.method == 'POST':
        resume.delete()
        messages.success(request, 'Rezyume o‘chirildi.')
        return redirect('resumes:list')
    
    return render(request, 'resumes/resume_confirm_delete.html', {'resume': resume})