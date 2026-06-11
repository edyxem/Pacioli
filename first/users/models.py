from django.contrib.auth.models import AbstractUser
from django.db import models

class Utilisateur(AbstractUser):
    ROLES = [
        ('admin', 'Administrateur'),
        ('comptable', 'Comptable'),
    ]
    role = models.CharField(max_length=20, choices=ROLES, default='comptable')