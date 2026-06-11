from django import forms
from .models import Depense
from tiers.models import Fournisseur

class DepenseForm(forms.ModelForm):
    class Meta:
        model = Depense
        fields = ['date', 'montant', 'description', 'fournisseur']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'montant': forms.NumberInput(attrs={'placeholder': 'Montant en XOF'}),
            'description': forms.TextInput(attrs={'placeholder': 'Description'}),
            'fournisseur': forms.Select(),
        }