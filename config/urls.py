"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# jobify/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    
    

    path('accounts/', include('accounts.urls')),
    path('profile/', include('profiles.urls')),
    path('resumes/', include('resumes.urls')),
    path('vacancies/', include('vacancies.urls')),
    path('applications/', include('applications.urls')),
    path('favorites/', include('favorites.urls')),
    path('notifications/', include('notifications.urls')),
    path('comments/', include('comments.urls')),
]

# Media va static fayllarni ishlab chiqish muhitida xizmat qilish
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)