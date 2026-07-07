# accounts/forms.py
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError

User = get_user_model()   # <-- Bu muhim!

class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Parol',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parol'})
    )
    password2 = forms.CharField(
        label='Parolni tasdiqlang',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parolni qayta kiriting'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'role')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Foydalanuvchi nomi'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Elektron pochta'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon raqam'}),
            'role': forms.Select(attrs={'class': 'form-control'}, choices=User.ROLE_CHOICES),
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError('Bu foydalanuvchi nomi allaqachon mavjud.')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Bu email allaqachon ro‘yxatdan o‘tgan.')
        return email

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if len(password) < 8:
            raise ValidationError('Parol kamida 8 belgidan iborat bo‘lishi kerak.')
        return password

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError('Parollar mos kelmadi.')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


# accounts/forms.py


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Foydalanuvchi nomi'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parol'})
    )