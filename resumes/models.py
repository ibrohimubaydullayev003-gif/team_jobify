# resumes/models.py
from django.db import models
from django.conf import settings
from .validators import validate_pdf_size 

def resume_upload_path(instance, filename):
    return f'resumes/{instance.candidate.id}/{filename}'

class Resume(models.Model):
    candidate = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='resumes')
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to=resume_upload_path, validators=[validate_pdf_size])
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.candidate.username} - {self.title}"