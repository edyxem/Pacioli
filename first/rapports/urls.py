from django.urls import path
from . import views

urlpatterns = [
    path('journal/', views.journal, name='journal'),
    path('bilan/', views.bilan, name='bilan'),
    path('bilan/pdf/', views.bilan_pdf, name='bilan_pdf'),
]