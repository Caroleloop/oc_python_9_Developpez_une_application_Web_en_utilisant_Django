from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm, CustomAuthenticationForm, FollowUserForm
from .models import UserFollows

User = get_user_model()


def login_view(request):
    """
    Affiche le formulaire de connexion et gère la soumission du formulaire.
    Si l'utilisateur est déjà connecté, il est redirigé vers le feed principal.

    Méthodes acceptées : GET, POST

    - GET : Affiche le formulaire de connexion vide.
    - POST : Valide les données de connexion et connecte l'utilisateur.
    """
    if request.user.is_authenticated:
        # Redirection si utilisateur déjà connecté
        return redirect("feed")

    # Initialisation du formulaire de connexion vide
    login_form = CustomAuthenticationForm()

    if request.method == "POST":
        # Remplissage du formulaire avec les données reçues
        login_form = CustomAuthenticationForm(data=request.POST)

        if login_form.is_valid():
            # Récupération et connexion de l'utilisateur authentifié
            user = login_form.get_user()
            login(request, user)
            return redirect("feed")
        else:
            # Affichage des erreurs dans la console pour debug
            print(login_form.errors)

    # Affichage du formulaire (GET ou en cas d'erreur)
    return render(
        request,
        "accounts/home.html",
        {"login_form": login_form},
    )


def signup_view(request):
    """
    Affiche le formulaire d'inscription et gère la création d'un nouvel utilisateur.

    Méthodes acceptées : GET, POST

    - GET : Affiche un formulaire d'inscription vide.
    - POST : Valide et crée un nouvel utilisateur, puis le connecte automatiquement.
    """
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            # Sauvegarde de l'utilisateur et connexion automatique
            user = form.save()
            login(request, user)
            return redirect("feed")
    else:
        # Création d'un formulaire vide pour GET
        form = CustomUserCreationForm()

    # Affichage du formulaire d'inscription
    return render(request, "accounts/signup.html", {"form": form})


def logout_view(request):
    """
    Déconnecte l'utilisateur courant et redirige vers la page d'accueil.
    """
    logout(request)
    return redirect("home")


@login_required
def subscriptions_view(request):
    """
    Gère les abonnements de l'utilisateur connecté :
    - Affiche les utilisateurs suivis et les abonnés.
    - Permet de rechercher des utilisateurs.
    - Permet de suivre ou de se désabonner d'un utilisateur.

    Méthodes acceptées : GET, POST

    GET : Affiche la liste des abonnements, abonnés et résultats de recherche.
    POST : Traite l'action de suivre ou de ne plus suivre un utilisateur.
    """
    current_user = request.user
    query = request.GET.get("q", "")

    if request.method == "POST":
        if request.POST.get("action") == "unfollow":
            # Traitement de la désinscription
            user_id = request.POST.get("user_id")
            user_to_unfollow = get_object_or_404(User, id=user_id)
            UserFollows.objects.filter(user=current_user, followed_user=user_to_unfollow).delete()
            return redirect("subscriptions")
        else:
            # Traitement de l'abonnement via le formulaire
            form = FollowUserForm(request.POST)
            if form.is_valid():
                user_to_follow = form.cleaned_data["username"]
                # Eviter de s'abonner à soi-même
                if user_to_follow != current_user:
                    UserFollows.objects.get_or_create(user=current_user, followed_user=user_to_follow)
                return redirect("subscriptions")
    else:
        # Initialisation d'un formulaire vide en GET
        form = FollowUserForm()

    # Recherche des utilisateurs par nom d'utilisateur, exclusion de soi-même
    search_results = []
    if query:
        search_results = User.objects.filter(username__icontains=query).exclude(id=current_user.id)

    # Récupération des utilisateurs suivis par l'utilisateur courant
    following_relations = UserFollows.objects.filter(user=current_user)
    following = [relation.followed_user for relation in following_relations]

    # Récupération des utilisateurs qui suivent l'utilisateur courant
    followers_relations = UserFollows.objects.filter(followed_user=current_user)
    followers = [relation.user for relation in followers_relations]

    context = {
        "form": form,
        "following": following,
        "followers": followers,
        "search_results": search_results,
        "query": query,
    }

    # Rendu de la page des abonnements
    return render(request, "accounts/subscriptions.html", context)
