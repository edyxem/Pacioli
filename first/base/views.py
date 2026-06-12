from django.shortcuts import render, redirect
from django.db.models import Sum
from recettes.models import Recette
from depenses.models import Depense
from tiers.models import Client, Fournisseur
from datetime import timedelta, date
import json


def money_total(queryset):
    value = queryset.aggregate(total=Sum('montant'))['total']
    return float(value or 0)


def get_chart_data(mode='mois'):
    today = date.today()

    if mode == 'semaine':
        lundi = today - timedelta(days=today.weekday())
        jours = ['LUN', 'MAR', 'MER', 'JEU', 'VEN', 'SAM', 'DIM']
        data = []

        for i in range(7):
            jour = lundi + timedelta(days=i)
            recettes = money_total(Recette.objects.filter(date=jour))
            depenses = money_total(Depense.objects.filter(date=jour))
            data.append({
                'label': jours[i],
                'recettes': recettes,
                'depenses': depenses,
                'net': recettes - depenses,
            })
        return data

    if mode == 'semaines':
        data = []
        for i in range(6, -1, -1):
            debut = today - timedelta(days=today.weekday()) - timedelta(weeks=i)
            fin = debut + timedelta(days=6)
            recettes = money_total(Recette.objects.filter(date__gte=debut, date__lte=fin))
            depenses = money_total(Depense.objects.filter(date__gte=debut, date__lte=fin))
            data.append({
                'label': f'S{7 - i}',
                'recettes': recettes,
                'depenses': depenses,
                'net': recettes - depenses,
            })
        return data

    data = []
    mois_labels = ['JAN', 'FÉV', 'MAR', 'AVR', 'MAI', 'JUN', 'JUL', 'AOÛ', 'SEP', 'OCT', 'NOV', 'DÉC']

    for i in range(5, -1, -1):
        mois_target = today.month - i
        annee_target = today.year

        while mois_target <= 0:
            mois_target += 12
            annee_target -= 1

        recettes = money_total(Recette.objects.filter(date__year=annee_target, date__month=mois_target))
        depenses = money_total(Depense.objects.filter(date__year=annee_target, date__month=mois_target))

        data.append({
            'label': mois_labels[mois_target - 1],
            'recettes': recettes,
            'depenses': depenses,
            'net': recettes - depenses,
        })

    return data


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')

    chart_mode = request.GET.get('chart', 'mois')

    recettes_qs = Recette.objects.all().order_by('-date')
    depenses_qs = Depense.objects.all().order_by('-date')

    total_recettes = money_total(recettes_qs)
    total_depenses = money_total(depenses_qs)
    solde = total_recettes - total_depenses

    chart_data = get_chart_data(chart_mode)

    context = {
        'recettes': recettes_qs[:5],
        'depenses': depenses_qs[:5],
        'total_recettes': total_recettes,
        'total_depenses': total_depenses,
        'solde': solde,
        'nb_clients': Client.objects.count(),
        'nb_fournisseurs': Fournisseur.objects.count(),
        'chart_mode': chart_mode,
        'cash_labels_json': json.dumps([d['label'] for d in chart_data], ensure_ascii=False),
        'cash_recettes_json': json.dumps([d['recettes'] for d in chart_data]),
        'cash_depenses_json': json.dumps([d['depenses'] for d in chart_data]),
        'cash_net_json': json.dumps([d['net'] for d in chart_data]),
    }

    return render(request, 'dashboard.html', context)