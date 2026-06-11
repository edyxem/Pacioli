from django.shortcuts import render
from recettes.models import Recette
from depenses.models import Depense

def journal(request):
    recettes = Recette.objects.all()
    depenses = Depense.objects.all()
    return render(request, 'rapports/journal.html', {
        'recettes': recettes,
        'depenses': depenses,
    })

def bilan(request):
    total_recettes = sum(r.montant for r in Recette.objects.all())
    total_depenses = sum(d.montant for d in Depense.objects.all())
    solde = total_recettes - total_depenses
    return render(request, 'rapports/bilan.html', {
        'total_recettes': total_recettes,
        'total_depenses': total_depenses,
        'solde': solde,
    })

def bilan_pdf(request):
    pass