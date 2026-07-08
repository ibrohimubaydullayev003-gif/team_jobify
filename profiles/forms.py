from django import forms
from .models import CandidateProfile, CompanyProfile

class CandidateProfileForm(forms.ModelForm):
    class Meta:
        model = CandidateProfile
        fields = ('full_name', 'bio', 'skills', 'experience', 'education', 'location', 'phone', 'avatar')

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone and not phone.isdigit():
            raise forms.ValidationError('Telefon raqam faqat raqamlardan iborat bo‘lishi kerak.')
        return phone


class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = ('company_name', 'description', 'website', 'location', 'logo', 'phone')

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone and not phone.isdigit():
            raise forms.ValidationError('Telefon raqam faqat raqamlardan iborat bo‘lishi kerak.')
        return phone