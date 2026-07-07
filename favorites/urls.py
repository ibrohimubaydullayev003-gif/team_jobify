# favorites/urls.py
from django.urls import path
from . import views

app_name = 'favorites'

urlpatterns = [
    path('', views.favorite_list, name='list'),
    path('add/<int:vacancy_id>/', views.add_favorite, name='add'),
    path('remove/<int:vacancy_id>/', views.remove_favorite, name='remove'),
]