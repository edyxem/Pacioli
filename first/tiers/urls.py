from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.liste_clients, name='liste_clients'),
    path('clients/<int:pk>/', views.detail_client, name='detail_client'),
    path('clients/ajouter/', views.ajouter_client, name='ajouter_client'),
    path('clients/modifier/<int:pk>/', views.modifier_client, name='modifier_client'),
    path('clients/supprimer/<int:pk>/', views.supprimer_client, name='supprimer_client'),

    path('fournisseurs/', views.liste_fournisseurs, name='liste_fournisseurs'),
    path('fournisseurs/<int:pk>/', views.detail_fournisseur, name='detail_fournisseur'),
    path('fournisseurs/ajouter/', views.ajouter_fournisseur, name='ajouter_fournisseur'),
    path('fournisseurs/modifier/<int:pk>/', views.modifier_fournisseur, name='modifier_fournisseur'),
    path('fournisseurs/supprimer/<int:pk>/', views.supprimer_fournisseur, name='supprimer_fournisseur'),
]