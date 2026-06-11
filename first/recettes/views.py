from django.shortcuts import render, redirect, get_object_or_404
from .models import Recette
from .forms import RecetteForm

def liste_recettes(request):
    query = request.GET.get('q', '')
    recettes = Recette.objects.filter(description__icontains=query) if query else Recette.objects.all()
    return render(request, 'recettes/liste.html', {'recettes': recettes, 'query': query})

def ajouter_recette(request):
    form = RecetteForm()
    if request.method == 'POST':
        form = RecetteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_recettes')
    return render(request, 'recettes/form.html', {'form': form, 'titre': 'Ajouter une recette'})

def modifier_recette(request, pk):
    recette = get_object_or_404(Recette, pk=pk)
    form = RecetteForm(instance=recette)
    if request.method == 'POST':
        form = RecetteForm(request.POST, instance=recette)
        if form.is_valid():
            form.save()
            return redirect('liste_recettes')
    return render(request, 'recettes/form.html', {'form': form, 'titre': 'Modifier une recette'})

def supprimer_recette(request, pk):
    recette = get_object_or_404(Recette, pk=pk)
    if request.method == 'POST':
        recette.delete()
        return redirect('liste_recettes')
    return render(request, 'recettes/confirmer_suppression.html', {'objet': recette})