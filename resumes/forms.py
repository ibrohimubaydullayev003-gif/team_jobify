from django import forms
from .models import Resume
from .validators import validate_pdf_size

class ResumeForm(forms.ModelForm):
    file = forms.FileField(
        validators=[validate_pdf_size],
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
        help_text='Faqat PDF, maksimal 5 MB'
    )

    class Meta:
        model = Resume
        fields = ('title', 'file')
        