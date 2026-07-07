# apps/profiles/models.py
from django.db import models
from django.conf import settings

class CandidateProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='candidate_profile')
    full_name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    skills = models.CharField(max_length=255, blank=True)
    experience = models.TextField(blank=True)
    education = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return f"Candidate: {self.user.username}"

class CompanyProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='company_profile')
    company_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.company_name