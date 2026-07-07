# vacancies/urls.py
from django.urls import path
from . import views

app_name = 'vacancies'

urlpatterns = [
    path('', views.vacancy_list, name='list'),
    path('create/', views.vacancy_create, name='create'),
    path('<int:pk>/', views.vacancy_detail, name='detail'),
    path('<int:pk>/update/', views.vacancy_update, name='update'),
    path('<int:pk>/delete/', views.vacancy_delete, name='delete'),
]