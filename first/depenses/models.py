from django.db import models

class Depense(models.Model):
    date = models.DateField()
    montant = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.CharField(max_length=255)
    fournisseur = models.ForeignKey('tiers.Fournisseur', on_delete=models.SET_NULL, null=True, blank=True)