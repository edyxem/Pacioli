from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, SignupForm

def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Identifiants incorrects.')
    return render(request, 'users.html', {'action': 'login', 'form': form})

def signup_view(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Compte créé. Connectez-vous.')
            return redirect('login')
        else:
            messages.error(request, 'Veuillez corriger les erreurs.')
    return render(request, 'users.html', {'action': 'signup', 'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')