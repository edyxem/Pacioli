from django.db import models


class CategorieDepense(models.Model):
    nom = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Catégorie de dépense"
        verbose_name_plural = "Catégories de dépenses"
        ordering = ['nom']

    def __str__(self):
        return self.nom


class Depense(models.Model):
    date = models.DateField()
    montant = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.CharField(max_length=255)
    fournisseur = models.ForeignKey('tiers.Fournisseur', on_delete=models.SET_NULL, null=True, blank=True)
    categorie = models.ForeignKey(CategorieDepense, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.description