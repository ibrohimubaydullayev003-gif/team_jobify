from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from vacancies.models import Vacancy
from .models import Apply

@login_required
def apply_to_vacancy(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, pk=vacancy_id, is_active=True)
    
    if request.user.role != 'candidate':
        messages.error(request, 'Faqat nomzodlar ariza topshirishi mumkin.')
        return redirect('vacancies:detail', pk=vacancy_id)
    
    if vacancy.is_deadline_passed():
        messages.error(request, 'Vakansiya muddati o‘tgan.')
        return redirect('vacancies:detail', pk=vacancy_id)
    
    if Apply.objects.filter(candidate=request.user, vacancy=vacancy).exists():
        messages.warning(request, 'Siz allaqachon ariza topshirgansiz.')
        return redirect('vacancies:detail', pk=vacancy_id)
    
    if not request.user.resumes.exists():
        messages.error(request, 'Iltimos, avval rezyume yarating.')
        return redirect('resumes:create')
    
    Apply.objects.create(candidate=request.user, vacancy=vacancy)
    messages.success(request, 'Ariza muvaffaqiyatli topshirildi!')
    return redirect('applications:my_applications')

@login_required
def my_applications(request):
    applies = request.user.applications.select_related('vacancy').all()
    return render(request, 'applications/my_applications.html', {'applies': applies})

@login_required
def company_applications(request):
    if request.user.role != 'hr':
        messages.error(request, 'Ruxsat yo‘q.')
        return redirect('home')
    vacancies = request.user.company_profile.vacancies.all()
    applies = Apply.objects.filter(vacancy__in=vacancies).select_related('candidate', 'vacancy')
    return render(request, 'applications/company_applications.html', {'applies': applies})

@login_required
def update_application_status(request, apply_id):
    apply = get_object_or_404(Apply, pk=apply_id, vacancy__company__user=request.user)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(Apply.STATUS_CHOICES):
            apply.status = new_status
            apply.save()
            messages.success(request, 'Holat yangilandi.')
        else:
            messages.error(request, 'Noto‘g‘ri holat.')
    return redirect('applications:company_applications')