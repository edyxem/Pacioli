from django import forms
from .models import Recette, CategorieRecette


class CategorieRecetteForm(forms.ModelForm):
    class Meta:
        model = CategorieRecette
        fields = ['nom']
        widgets = {
            'nom': forms.TextInput(attrs={'placeholder': 'Ex: Ventes, Prestations...'}),
        }


class RecetteForm(forms.ModelForm):
    class Meta:
        model = Recette
        fields = ['date', 'montant', 'description', 'categorie', 'client']
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