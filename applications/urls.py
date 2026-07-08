from django.urls import path
from . import views

app_name = 'applications'

urlpatterns = [
    path('apply/<int:vacancy_id>/', views.apply_to_vacancy, name='apply'),
    path('my/', views.my_applications, name='my_applications'),
    path('company/', views.company_applications, name='company_applications'),
    path('update-status/<int:apply_id>/', views.update_application_status, name='update_status'),
]