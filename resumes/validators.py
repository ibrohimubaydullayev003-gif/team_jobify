from django.core.exceptions import ValidationError

def validate_pdf_size(value):
    if not value.name.endswith('.pdf'):
        raise ValidationError('Faqat PDF fayl yuklashingiz mumkin.')
    if value.size > 5 * 1024 * 1024:
        raise ValidationError('Fayl hajmi 5 MB dan oshmasligi kerak.')