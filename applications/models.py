# apps/applications/models.py
from django.db import models
from django.conf import settings
from vacancies.models import Vacancy

class Apply(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Ko‘rib chiqilmoqda'),
        ('viewed', 'Ko‘rilgan'),
        ('accepted', 'Qabul qilingan'),
        ('rejected', 'Rad etilgan'),
    )
    candidate = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='applications')
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('candidate', 'vacancy')  # bir martalik apply

    def __str__(self):
        return f"{self.candidate.username} -> {self.vacancy.title}"


