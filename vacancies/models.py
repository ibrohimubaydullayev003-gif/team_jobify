from django.db import models
from django.conf import settings
from profiles.models import CompanyProfile

class Vacancy(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, related_name='vacancies')
    title = models.CharField(max_length=255)
    description = models.TextField()
    salary_min = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    salary_max = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    location = models.CharField(max_length=200)
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_remote = models.BooleanField(default=False)
    requirements = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def is_deadline_passed(self):
        from django.utils import timezone
        return self.deadline < timezone.now().date()