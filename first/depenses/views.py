from django.shortcuts import render, redirect, get_object_or_404
from .models import Depense, CategorieDepense
from .forms import DepenseForm

def liste_depenses(request):
    query = request.GET.get('q', '')
    categorie_id = request.GET.get('categorie', '')
    depenses = Depense.objects.all()
    if query:
        depenses = depenses.filter(description__icontains=query)
    if categorie_id:
        depenses = depenses.filter(categorie_id=categorie_id)
    total_depenses = sum(d.montant for d in depenses)
    categories = CategorieDepense.objects.all()
    return render(request, 'depenses.html', {
        'action': 'liste',
        'depenses': depenses,
        'query': query,
        'total_depenses': total_depenses,
        'categories': categories,
        'categorie_active': categorie_id,
    })


def detail_depense(request, pk):
    depense = get_object_or_404(Depense, pk=pk)
    return render(request, 'depenses.html', {
        'action': 'detail',
        'depense': depense,
    })


def ajouter_depense(request):
    form = DepenseForm()
    if request.method == 'POST':
        form = DepenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_depenses')
    return render(request, 'depenses.html', {
        'action': 'form',
        'form': form,
        'titre': 'Ajouter une dépense',
    })


def modifier_depense(request, pk):
    depense = get_object_or_404(Depense, pk=pk)
    form = DepenseForm(instance=depense)
    if request.method == 'POST':
        form = DepenseForm(request.POST, instance=depense)
        if form.is_valid():
            form.save()
            return redirect('liste_depenses')
    return render(request, 'depenses.html', {
        'action': 'form',
        'form': form,
        'titre': 'Modifier une dépense',
    })


def supprimer_depense(request, pk):
    depense = get_object_or_404(Depense, pk=pk)
    if request.method == 'POST':
        depense.delete()
        return redirect('liste_depenses')
    return render(request, 'depenses.html', {
        'action': 'supprimer',
        'objet': depense,
        'retour': 'liste_depenses',
    })