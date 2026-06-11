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

    def clean_nom(self):
        nom = self.cleaned_data.get('nom')
        if not nom.strip():
            raise forms.ValidationError('Le nom du client est obligatoire.')
        return nom

    def clean_telephone(self):
        telephone = self.cleaned_data.get('telephone')
        # Vérification doublon téléphone (LM6)
        qs = Client.objects.filter(telephone=telephone)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError('Un client avec ce numéro existe déjà.')
        return telephone


class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields = ['nom', 'telephone', 'adresse']
        widgets = {
            'nom': forms.TextInput(attrs={'placeholder': 'Nom du fournisseur'}),
            'telephone': forms.TextInput(attrs={'placeholder': 'Téléphone'}),
            'adresse': forms.TextInput(attrs={'placeholder': 'Adresse'}),
        }

    def clean_nom(self):
        nom = self.cleaned_data.get('nom')
        if not nom.strip():
            raise forms.ValidationError('Le nom du fournisseur est obligatoire.')
        return nom

    def clean_telephone(self):
        telephone = self.cleaned_data.get('telephone')
        # Vérification doublon téléphone (LM7)
        qs = Fournisseur.objects.filter(telephone=telephone)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError('Un fournisseur avec ce numéro existe déjà.')
        return telephone