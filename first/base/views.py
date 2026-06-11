from django.shortcuts import render
from recettes.models import Recette
from depenses.models import Depense

def dashboard(request):
    recettes = Recette.objects.all()
    depenses = Depense.objects.all()

    total_recettes = sum(r.montant for r in recettes)
    total_depenses = sum(d.montant for d in depenses)
    solde = total_recettes - total_depenses

    context = {
        'recettes': recettes[:5],
        'depenses': depenses[:5],
        'total_recettes': total_recettes,
        'total_depenses': total_depenses,
        'solde': solde,
    }
    return render(request, 'base/dashboard.html', context)