from django.shortcuts import render, redirect, get_object_or_404
from .models import Depense
from .forms import DepenseForm

def liste_depenses(request):
    query = request.GET.get('q', '')
    depenses = Depense.objects.filter(description__icontains=query) if query else Depense.objects.all()
    return render(request, 'depenses/liste.html', {'depenses': depenses, 'query': query})

def ajouter_depense(request):
    form = DepenseForm()
    if request.method == 'POST':
        form = DepenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_depenses')
    return render(request, 'depenses/form.html', {'form': form, 'titre': 'Ajouter une dépense'})

def modifier_depense(request, pk):
    depense = get_object_or_404(Depense, pk=pk)
    form = DepenseForm(instance=depense)
    if request.method == 'POST':
        form = DepenseForm(request.POST, instance=depense)
        if form.is_valid():
            form.save()
            return redirect('liste_depenses')
    return render(request, 'depenses/form.html', {'form': form, 'titre': 'Modifier une dépense'})

def supprimer_depense(request, pk):
    depense = get_object_or_404(Depense, pk=pk)
    if request.method == 'POST':
        depense.delete()
        return redirect('liste_depenses')
    return render(request, 'depenses/confirmer_suppression.html', {'objet': depense})