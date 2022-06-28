from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label='Contraseña',
        max_length=50,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña',
                'class': 'form-control',
                'data-toggle': 'password',
                'id': 'password',
                }))
    password2 = forms.CharField(
        label='Confirmación de contraseña',
        max_length=50,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirmación de contraseña',
                'class': 'form-control',
                'data-toggle': 'password',
                'id': 'password',
                }))  
    class Meta:
        model = CustomUser
        fields = ('dni', 'nombres', 'apellidos', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('dni', 'nombres', 'apellidos', 'email')