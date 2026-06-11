from django.shortcuts import render
from recettes.models import Recette
from depenses.models import Depense

def journal(request):
    # Filtres par date et type (LM8)
    date_debut = request.GET.get('date_debut', '')
    date_fin = request.GET.get('date_fin', '')
    type_op = request.GET.get('type', '')

    recettes = Recette.objects.all()
    depenses = Depense.objects.all()

    if date_debut:
        recettes = recettes.filter(date__gte=date_debut)
        depenses = depenses.filter(date__gte=date_debut)
    if date_fin:
        recettes = recettes.filter(date__lte=date_fin)
        depenses = depenses.filter(date__lte=date_fin)

    return render(request, 'rapports/journal.html', {
        'recettes': recettes,
        'depenses': depenses,
        'date_debut': date_debut,
        'date_fin': date_fin,
        'type_op': type_op,
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

def etat_recettes(request):
    recettes = Recette.objects.all()
    total = sum(r.montant for r in recettes)
    return render(request, 'rapports/etat_recettes.html', {
        'recettes': recettes,
        'total': total,
    })

def etat_depenses(request):
    depenses = Depense.objects.all()
    total = sum(d.montant for d in depenses)
    return render(request, 'rapports/etat_depenses.html', {
        'depenses': depenses,
        'total': total,
    })

def rapport_global(request):
    total_recettes = sum(r.montant for r in Recette.objects.all())
    total_depenses = sum(d.montant for d in Depense.objects.all())
    solde = total_recettes - total_depenses
    recettes = Recette.objects.all()
    depenses = Depense.objects.all()
    return render(request, 'rapports/rapport_global.html', {
        'total_recettes': total_recettes,
        'total_depenses': total_depenses,
        'solde': solde,
        'recettes': recettes,
        'depenses': depenses,
    })

def bilan_pdf(request):
    pass