from django.shortcuts import render, redirect, get_object_or_404
from .models import Recette, CategorieRecette
from .forms import RecetteForm, CategorieRecetteForm


def liste_recettes(request):
    query = request.GET.get('q', '')
    categorie_id = request.GET.get('categorie', '')
    recettes = Recette.objects.all()
    if query:
        recettes = recettes.filter(description__icontains=query)
    if categorie_id:
        recettes = recettes.filter(categorie_id=categorie_id)
    total_recettes = sum(r.montant for r in recettes)
    categories = CategorieRecette.objects.all()
    return render(request, 'recettes.html', {
        'action': 'liste',
        'recettes': recettes,
        'query': query,
        'total_recettes': total_recettes,
        'categories': categories,
        'categorie_active': categorie_id,
    })


def detail_recette(request, pk):
    recette = get_object_or_404(Recette, pk=pk)
    return render(request, 'recettes.html', {
        'action': 'detail',
        'recette': recette,
    })


def ajouter_recette(request):
    form = RecetteForm()
    if request.method == 'POST':
        form = RecetteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_recettes')
    return render(request, 'recettes.html', {
        'action': 'form',
        'form': form,
        'titre': 'Ajouter une recette',
    })


def modifier_recette(request, pk):
    recette = get_object_or_404(Recette, pk=pk)
    form = RecetteForm(instance=recette)
    if request.method == 'POST':
        form = RecetteForm(request.POST, instance=recette)
        if form.is_valid():
            form.save()
            return redirect('liste_recettes')
    return render(request, 'recettes.html', {
        'action': 'form',
        'form': form,
        'titre': 'Modifier une recette',
    })


def supprimer_recette(request, pk):
    recette = get_object_or_404(Recette, pk=pk)
    if request.method == 'POST':
        recette.delete()
        return redirect('liste_recettes')
    return render(request, 'recettes.html', {
        'action': 'supprimer',
        'objet': recette,
        'retour': 'liste_recettes',
    })