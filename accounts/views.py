from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
User = get_user_model()
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Connexion réussie.')
            if user.is_superuser:
                return redirect('admin:index')  # Rediriger vers la page d'administration
            else:
                return redirect('index')  # Rediriger vers la page utilisateur normale
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')

    return render(request, "login.html")

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('index',)
    return render(request, "signup.html")

def logout_user(request):
    logout(request)
    return redirect('index')

def profil_user(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        username = request.POST.get("username")
        user = request.user
        user.first_name = firstname
        user.last_name = lastname
        user.email = email
        user.username = username
        user.save()

        messages.success(request, 'Votre profil a été mis à jour avec succès.')
        return redirect('index')
    return render(request, "profil.html")