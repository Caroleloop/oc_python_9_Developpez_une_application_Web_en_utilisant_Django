from django.contrib.auth import login
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout


def login_view(request):



    # Initialisation du formulaire de connexion vide
    login_form = CustomAuthenticationForm()

    # Si le formulaire est soumis en méthode POST
    if request.method == "POST":
        # On remplit le formulaire avec les données reçues
        login_form = CustomAuthenticationForm(data=request.POST)

        # Validation des données du formulaire
        if login_form.is_valid():
            # Récupération de l'utilisateur connecté
            user = login_form.get_user()

            # Connexion de l'utilisateur dans la session
            login(request, user)

            # Redirection vers la page principale (feed)
            return redirect("feed")
        else:
            # En cas d'erreur, on affiche les erreurs dans la console (pour debug)
            print(login_form.errors)

    # Affichage du template avec le formulaire de connexion (GET ou en cas d'erreur)
    return render(
        request,
        "accounts/home.html",
        {
            "login_form": login_form,
        },
    )


def signup_view(request):
    # Si formulaire soumis en POST, on traite les données reçues
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        # Validation du formulaire
        if form.is_valid():
            # Sauvegarde du nouvel utilisateur en base
            user = form.save()

            # Connexion automatique du nouvel utilisateur
            login(request, user)

            # Redirection vers la page principale (feed)
            return redirect("feed")
    else:
        # Si méthode GET, on crée un formulaire vide
        form = CustomUserCreationForm()

    # Affichage du formulaire d'inscription dans le template
    return render(request, "accounts/signup.html", {"form": form})


def logout_view(request):
    # Déconnexion de l'utilisateur
    logout(request)

    # Redirection vers la page d'accueil
    return redirect("home")
