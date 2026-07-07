# apps/vacancies/forms.py
from django import forms
from .models import Vacancy

class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ('title', 'description', 'salary_min', 'salary_max', 'location', 'deadline', 'is_remote', 'requirements')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'salary_min': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Minimal maosh'}),
            'salary_max': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Maksimal maosh'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'deadline': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'is_remote': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'requirements': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

    def clean(self):
        cleaned_data = super().clean()
        salary_min = cleaned_data.get('salary_min')
        salary_max = cleaned_data.get('salary_max')
        if salary_min and salary_max and salary_min > salary_max:
            raise forms.ValidationError('Minimal maosh maksimal maoshdan katta bo‘lishi mumkin emas.')
        return cleaned_data