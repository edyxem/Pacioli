from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Utilisateur

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': "Nom d'utilisateur",
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Mot de passe',
        })
    )

class SignupForm(UserCreationForm):
    class Meta:
        model = Utilisateur
        fields = ['username', 'email', 'role', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': "Nom d'utilisateur"}),
            'email': forms.EmailInput(attrs={'placeholder': 'Adresse e-mail'}),
        }