from django.db import models

class Client(models.Model):
    nom = models.CharField(max_length=150)
    telephone = models.CharField(max_length=20)
    adresse = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

class Fournisseur(models.Model):
    nom = models.CharField(max_length=150)
    telephone = models.CharField(max_length=20)
    adresse = models.CharField(max_length=255)

    def __str__(self):
        return self.nom