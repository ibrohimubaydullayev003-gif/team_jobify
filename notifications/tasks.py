# apps/notifications/tasks.py
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model
from vacancies.models import Vacancy

User = get_user_model()

@shared_task
def send_application_notification(candidate_id, vacancy_id):
    candidate = User.objects.get(id=candidate_id)
    vacancy = Vacancy.objects.get(id=vacancy_id)
    subject = f"Ariza topshirdingiz: {vacancy.title}"
    message = f"Siz {vacancy.title} vakansiyasiga ariza topshirdingiz. Kompaniya siz bilan bog‘lanadi."
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [candidate.email])

@shared_task
def send_status_update_notification(candidate_id, vacancy_id, new_status):
    candidate = User.objects.get(id=candidate_id)
    vacancy = Vacancy.objects.get(id=vacancy_id)
    status_map = dict(Apply.STATUS_CHOICES)
    subject = f"Ariza holati o‘zgardi: {vacancy.title}"
    message = f"Sizning {vacancy.title} vakansiyasiga arizangiz holati: {status_map.get(new_status, new_status)}"
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [candidate.email])