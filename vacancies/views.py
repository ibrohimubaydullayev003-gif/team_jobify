# vacancies/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Vacancy
from .forms import VacancyForm

@login_required
def vacancy_list(request):
    query = request.GET.get('q')
    location = request.GET.get('location')
    remote = request.GET.get('remote')
    # ✅ Tartiblash qo‘shildi
    vacancies = Vacancy.objects.filter(is_active=True).order_by('-created_at')

    if query:
        vacancies = vacancies.filter(
            Q(title__icontains=query) | Q(company__company_name__icontains=query)
        )
    if location:
        vacancies = vacancies.filter(location__icontains=location)
    if remote:
        vacancies = vacancies.filter(is_remote=True)

    paginator = Paginator(vacancies, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'vacancies/vacancy_list.html', {'page_obj': page_obj})

@login_required
def vacancy_create(request):
    if request.user.role != 'hr':
        messages.error(request, 'Sizda vakansiya joylash huquqi yo‘q.')
        return redirect('home')
    if request.method == 'POST':
        form = VacancyForm(request.POST)
        if form.is_valid():
            vacancy = form.save(commit=False)
            vacancy.company = request.user.company_profile
            vacancy.save()
            messages.success(request, 'Vakansiya yaratildi!')
            # ✅ To‘g‘ri redirect
            return redirect('vacancies:list')
    else:
        form = VacancyForm()
    return render(request, 'vacancies/vacancy_form.html', {'form': form, 'action': 'Yaratish'})

@login_required
def vacancy_update(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk, company__user=request.user)
    if request.method == 'POST':
        form = VacancyForm(request.POST, instance=vacancy)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vakansiya yangilandi!')
            # ✅ To‘g‘ri redirect
            return redirect('vacancies:list')
    else:
        form = VacancyForm(instance=vacancy)
    return render(request, 'vacancies/vacancy_form.html', {'form': form, 'action': 'Yangilash'})

@login_required
def vacancy_delete(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk, company__user=request.user)
    if request.method == 'POST':
        vacancy.delete()
        messages.success(request, 'Vakansiya o‘chirildi.')
        # ✅ To‘g‘ri redirect
        return redirect('vacancies:list')
    return render(request, 'vacancies/vacancy_confirm_delete.html', {'vacancy': vacancy})

@login_required
def vacancy_detail(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk, is_active=True)
    applied = False
    if request.user.role == 'candidate':
        # ✅ `apply_set` – default related_name (model nomi `Apply` bo‘lgani uchun)
        applied = vacancy.apply_set.filter(candidate=request.user).exists()
    return render(request, 'vacancies/vacancy_detail.html', {'vacancy': vacancy, 'applied': applied})