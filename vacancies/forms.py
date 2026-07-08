from django import forms
from .models import Vacancy

class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ('title', 'description', 'salary_min', 'salary_max', 'location', 'deadline', 'is_remote', 'requirements')

    def clean(self):
        cleaned_data = super().clean()
        salary_min = cleaned_data.get('salary_min')
        salary_max = cleaned_data.get('salary_max')
        if salary_min and salary_max and salary_min > salary_max:
            raise forms.ValidationError('Minimal maosh maksimal maoshdan katta bo‘lishi mumkin emas.')
        return cleaned_data