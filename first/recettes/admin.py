from django.contrib import admin
from .models import Recette, CategorieRecette

admin.site.register(CategorieRecette)
admin.site.register(Recette)