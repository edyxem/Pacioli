from django import forms
from .models import Recette
from tiers.models import Client

class RecetteForm(forms.ModelForm):
    class Meta:
        model = Recette
        fields = ['date', 'montant', 'description', 'client']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'montant': forms.NumberInput(attrs={'placeholder': 'Montant en XOF'}),
            'description': forms.TextInput(attrs={'placeholder': 'Description'}),
            'client': forms.Select(),
        }