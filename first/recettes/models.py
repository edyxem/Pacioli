from django.db import models


class CategorieRecette(models.Model):
    nom = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Catégorie de recette"
        verbose_name_plural = "Catégories de recettes"
        ordering = ['nom']

    def __str__(self):
        return self.nom


class Recette(models.Model):
    date = models.DateField()
    montant = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.CharField(max_length=255)
    client = models.ForeignKey('tiers.Client', on_delete=models.SET_NULL, null=True, blank=True)
    categorie = models.ForeignKey(CategorieRecette, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.description