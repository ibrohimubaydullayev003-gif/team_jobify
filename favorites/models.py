from django.db import models
from django.conf import settings
from vacancies.models import Vacancy

class Favorite(models.Model):
    candidate = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favorites')
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('candidate', 'vacancy')

    def __str__(self):
        return f"{self.candidate.username} -> {self.vacancy.title}"