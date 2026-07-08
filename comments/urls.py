from django.urls import path
from . import views

app_name = 'comments'

urlpatterns = [
    path('add/<int:vacancy_id>/', views.add_comment, name='add'),
    path('delete/<int:comment_id>/', views.delete_comment, name='delete'),
    path('edit/<int:comment_id>/', views.edit_comment, name='edit'),
]