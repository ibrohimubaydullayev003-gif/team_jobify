# apps/accounts/urls.py
from django.urls import path
from .views import *

app_name = 'accounts'
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('change-password/', change_password, name='change_password'),
]


