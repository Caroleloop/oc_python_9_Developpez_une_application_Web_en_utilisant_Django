from django.urls import path
from . import views


def get_urlpatterns():
    """
    Définit la liste des routes URL pour l'application.

    Chaque route associe une URL à une vue spécifique, avec un nom
    pour faciliter leur utilisation dans les templates ou la logique Django.

    Returns:
        list: Une liste d'objets path configurant les routes URL.
    """
    # Liste des routes URL de l'application
    urlpatterns = [
        # Route racine ("/"), affiche la page de connexion via la vue login_view
        # Nom de la route : "login"
        path("", views.login_view, name="login"),
        # Route "/signup/", affiche la page d'inscription via la vue signup_view
        # Nom de la route : "signup"
        path("signup/", views.signup_view, name="signup"),
        # Route "/logout/", permet la déconnexion via la vue logout_view
        # Nom de la route : "logout"
        path("logout/", views.logout_view, name="logout"),
        # Route "/subscriptions/", affiche la page des abonnements via subscriptions_view
        # Nom de la route : "subscriptions"
        path("subscriptions/", views.subscriptions_view, name="subscriptions"),
    ]

    return urlpatterns


# Liste des routes URL exportée pour être utilisée dans le projet Django
urlpatterns = get_urlpatterns()
