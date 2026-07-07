# apps/resumes/urls.py
from django.urls import path
from . import views

app_name = 'resumes'

urlpatterns = [
    path('', views.resume_list, name='list'),
    path('create/', views.resume_create, name='create'),
    path('<int:pk>/update/', views.resume_update, name='update'),
    path('<int:pk>/delete/', views.resume_delete, name='delete'),
]