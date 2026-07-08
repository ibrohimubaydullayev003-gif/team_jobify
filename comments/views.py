from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from vacancies.models import Vacancy
from .models import Comment
from .forms import CommentForm

@login_required
def add_comment(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, pk=vacancy_id, is_active=True)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.vacancy = vacancy
            
            parent_id = request.POST.get('parent_id')
            if parent_id:
                try:
                    parent = Comment.objects.get(pk=parent_id, vacancy=vacancy, is_active=True)
                    comment.parent = parent
                except Comment.DoesNotExist:
                    pass
            
            comment.save()
            messages.success(request, 'Fikr qoldirildi!')
        else:
            messages.error(request, 'Fikr qoldirishda xatolik yuz berdi.')
    else:
        messages.error(request, 'Noto‘g‘ri so‘rov.')
    
    return redirect('vacancies:detail', pk=vacancy_id)

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id, user=request.user)
    
    if request.method == 'POST':
        comment.is_active = False
        comment.save()
        messages.success(request, 'Fikr o‘chirildi.')
    else:
        messages.error(request, 'Noto‘g‘ri so‘rov.')
    
    return redirect('vacancies:detail', pk=comment.vacancy.id)

@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id, user=request.user, is_active=True)
    
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fikr yangilandi!')
            return redirect('vacancies:detail', pk=comment.vacancy.id)
    else:
        form = CommentForm(instance=comment)
    
    return render(request, 'comments/edit_comment.html', {
        'form': form,
        'comment': comment,
        'vacancy': comment.vacancy
    })