from django.shortcuts import render, redirect, get_object_or_404
from .models import Client, Fournisseur
from .forms import ClientForm, FournisseurForm

def liste_clients(request):
    query = request.GET.get('q', '')
    clients = Client.objects.filter(nom__icontains=query) if query else Client.objects.all()
    return render(request, 'tiers/clients.html', {'clients': clients, 'query': query})

def detail_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'tiers/detail_client.html', {'client': client})

def ajouter_client(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_clients')
    return render(request, 'tiers/form_client.html', {'form': form, 'titre': 'Ajouter un client'})

def modifier_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    form = ClientForm(instance=client)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('liste_clients')
    return render(request, 'tiers/form_client.html', {'form': form, 'titre': 'Modifier un client'})

def supprimer_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('liste_clients')
    return render(request, 'tiers/confirmer_suppression.html', {'objet': client})

def liste_fournisseurs(request):
    query = request.GET.get('q', '')
    fournisseurs = Fournisseur.objects.filter(nom__icontains=query) if query else Fournisseur.objects.all()
    return render(request, 'tiers/fournisseurs.html', {'fournisseurs': fournisseurs, 'query': query})

def detail_fournisseur(request, pk):
    fournisseur = get_object_or_404(Fournisseur, pk=pk)
    return render(request, 'tiers/detail_fournisseur.html', {'fournisseur': fournisseur})

def ajouter_fournisseur(request):
    form = FournisseurForm()
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_fournisseurs')
    return render(request, 'tiers/form_fournisseur.html', {'form': form, 'titre': 'Ajouter un fournisseur'})

def modifier_fournisseur(request, pk):
    fournisseur = get_object_or_404(Fournisseur, pk=pk)
    form = FournisseurForm(instance=fournisseur)
    if request.method == 'POST':
        form = FournisseurForm(request.POST, instance=fournisseur)
        if form.is_valid():
            form.save()
            return redirect('liste_fournisseurs')
    return render(request, 'tiers/form_fournisseur.html', {'form': form, 'titre': 'Modifier un fournisseur'})

def supprimer_fournisseur(request, pk):
    fournisseur = get_object_or_404(Fournisseur, pk=pk)
    if request.method == 'POST':
        fournisseur.delete()
        return redirect('liste_fournisseurs')
    return render(request, 'tiers/confirmer_suppression.html', {'objet': fournisseur})