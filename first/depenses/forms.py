from django import forms
from .models import Depense, CategorieDepense


class CategorieDepenseForm(forms.ModelForm):
    class Meta:
        model = CategorieDepense
        fields = ['nom']
        widgets = {
            'nom': forms.TextInput(attrs={'placeholder': 'Ex: Loyer, Fournitures...'}),
        }


class DepenseForm(forms.ModelForm):
    class Meta:
        model = Depense
        fields = ['date', 'montant', 'description', 'categorie', 'fournisseur']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'montant': forms.NumberInput(attrs={'placeholder': 'Montant en XOF'}),
            'description': forms.TextInput(attrs={'placeholder': 'Description'}),
        }

    def clean_montant(self):
        montant = self.cleaned_data.get('montant')
        if montant <= 0:
            raise forms.ValidationError('Le montant doit être supérieur à 0.')
        return montant

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if not description.strip():
            raise forms.ValidationError('La description est obligatoire.')
        return description