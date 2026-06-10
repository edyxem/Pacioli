from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_recettes, name='liste_recettes'),
    path('ajouter/', views.ajouter_recette, name='ajouter_recette'),
    path('modifier/<int:pk>/', views.modifier_recette, name='modifier_recette'),
    path('supprimer/<int:pk>/', views.supprimer_recette, name='supprimer_recette'),
]