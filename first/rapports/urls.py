from django.urls import path
from . import views

urlpatterns = [
    path('journal/', views.journal, name='journal'),
    path('bilan/', views.bilan, name='bilan'),
    path('bilan/pdf/', views.bilan_pdf, name='bilan_pdf'),
    path('recettes/', views.etat_recettes, name='etat_recettes'),
    path('depenses/', views.etat_depenses, name='etat_depenses'),
    path('global/', views.rapport_global, name='rapport_global'),
]