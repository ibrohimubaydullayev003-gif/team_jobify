from django import forms
from .models import Apply

class ApplicationStatusForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ('status',)
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}, choices=Apply.STATUS_CHOICES),
        }