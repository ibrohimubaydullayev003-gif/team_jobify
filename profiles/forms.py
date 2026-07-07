# apps/profiles/forms.py
from django import forms
from .models import CandidateProfile, CompanyProfile

class CandidateProfileForm(forms.ModelForm):
    class Meta:
        model = CandidateProfile
        fields = ('full_name', 'bio', 'skills', 'experience', 'education', 'location', 'phone', 'avatar')
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'skills': forms.TextInput(attrs={'class': 'form-control'}),
            'experience': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'education': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone and not phone.isdigit():
            raise forms.ValidationError('Telefon raqam faqat raqamlardan iborat bo‘lishi kerak.')
        return phone


class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = ('company_name', 'description', 'website', 'location', 'logo', 'phone')
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://...'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'logo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone and not phone.isdigit():
            raise forms.ValidationError('Telefon raqam faqat raqamlardan iborat bo‘lishi kerak.')
        return phone