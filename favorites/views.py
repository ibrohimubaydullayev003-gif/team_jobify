from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Favorite
from vacancies.models import Vacancy

@login_required
def favorite_list(request):
    favorites = request.user.favorites.select_related('vacancy').all()
    return render(request, 'favorites/list.html', {'favorites': favorites})

@login_required
def add_favorite(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, pk=vacancy_id)
    Favorite.objects.get_or_create(candidate=request.user, vacancy=vacancy)
    messages.success(request, "Vakansiya sevimlilarga qo‘shildi.")
    return redirect('vacancies:detail', pk=vacancy_id)

@login_required
def remove_favorite(request, vacancy_id):
    Favorite.objects.filter(candidate=request.user, vacancy_id=vacancy_id).delete()
    messages.success(request, "Vakansiya sevimlilardan olib tashlandi.")
    return redirect('vacancies:detail', pk=vacancy_id)