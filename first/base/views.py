from django.shortcuts import render, redirect
from django.utils import timezone
from recettes.models import Recette
from depenses.models import Depense
from tiers.models import Client, Fournisseur
from datetime import timedelta, date
from decimal import Decimal


def get_chart_data(mode='mois'):
    today = date.today()

    if mode == 'semaine':
        # Lundi de la semaine courante
        lundi = today - timedelta(days=today.weekday())
        jours = ['LUN', 'MAR', 'MER', 'JEU', 'VEN', 'SAM', 'DIM']
        data = []
        for i in range(7):
            jour = lundi + timedelta(days=i)
            recettes = sum(r.montant for r in Recette.objects.filter(date=jour))
            depenses = sum(d.montant for d in Depense.objects.filter(date=jour))
            data.append({
                'label': jours[i],
                'recettes': float(recettes),
                'depenses': float(depenses),
                'net': float(recettes - depenses),
            })
        return data

    elif mode == 'semaines':
        # 7 dernières semaines
        data = []
        for i in range(6, -1, -1):
            debut = today - timedelta(days=today.weekday()) - timedelta(weeks=i)
            fin = debut + timedelta(days=6)
            recettes = sum(r.montant for r in Recette.objects.filter(date__gte=debut, date__lte=fin))
            depenses = sum(d.montant for d in Depense.objects.filter(date__gte=debut, date__lte=fin))
            data.append({
                'label': f'S{7 - i}',
                'recettes': float(recettes),
                'depenses': float(depenses),
                'net': float(recettes - depenses),
            })
        return data

    else:  # mois — 6 derniers mois
        data = []
        MOIS = ['JAN', 'FÉV', 'MAR', 'AVR', 'MAI', 'JUN', 'JUL', 'AOÛ', 'SEP', 'OCT', 'NOV', 'DÉC']
        for i in range(5, -1, -1):
            # Calculer le mois cible
            mois_target = today.month - i
            annee_target = today.year
            while mois_target <= 0:
                mois_target += 12
                annee_target -= 1
            recettes = sum(r.montant for r in Recette.objects.filter(
                date__year=annee_target, date__month=mois_target))
            depenses = sum(d.montant for d in Depense.objects.filter(
                date__year=annee_target, date__month=mois_target))
            data.append({
                'label': MOIS[mois_target - 1],
                'recettes': float(recettes),
                'depenses': float(depenses),
                'net': float(recettes - depenses),
            })
        return data


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')

    # Mode graphique actif
    chart_mode = request.GET.get('chart', 'mois')

    recettes = Recette.objects.all()
    depenses = Depense.objects.all()
    total_recettes = sum(r.montant for r in recettes)
    total_depenses = sum(d.montant for d in depenses)
    solde = total_recettes - total_depenses

    chart_data = get_chart_data(chart_mode)

    # Calcul hauteur des barres (max = 100%)
    max_val = max((d['recettes'] for d in chart_data), default=1)
    if max_val == 0:
        max_val = 1
    for d in chart_data:
        d['hauteur'] = round((d['recettes'] / max_val) * 90) + 5  # min 5%, max 95%

    return render(request, 'dashboard.html', {
        'recettes': recettes[:5],
        'depenses': depenses[:5],
        'total_recettes': total_recettes,
        'total_depenses': total_depenses,
        'solde': solde,
        'nb_clients': Client.objects.count(),
        'nb_fournisseurs': Fournisseur.objects.count(),
        'chart_data': chart_data,
        'chart_mode': chart_mode,
    })