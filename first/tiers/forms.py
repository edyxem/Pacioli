from django import forms
from .models import Client, Fournisseur

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['nom', 'telephone', 'adresse']
        widgets = {
            'nom': forms.TextInput(attrs={'placeholder': 'Nom du client'}),
            'telephone': forms.TextInput(attrs={'placeholder': 'Téléphone'}),
            'adresse': forms.TextInput(attrs={'placeholder': 'Adresse'}),
        }

class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields = ['nom', 'telephone', 'adresse']
        widgets = {
            'nom': forms.TextInput(attrs={'placeholder': 'Nom du fournisseur'}),
            'telephone': forms.TextInput(attrs={'placeholder': 'Téléphone'}),
            'adresse': forms.TextInput(attrs={'placeholder': 'Adresse'}),
        }