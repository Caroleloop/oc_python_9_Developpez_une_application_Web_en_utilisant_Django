from django.urls import path
from . import views
from .views import feed_view


# Liste des routes URL de l'application
urlpatterns = [
    # Route racine, associe la vue login_view et nomme cette URL "login"
    path("", views.login_view, name="login"),
    # Route pour l'inscription, associe la vue signup_view et nomme cette URL "signup"
    path("signup/", views.signup_view, name="signup"),
    # Route pour le fil d'actualité, associe la vue feed_view et nomme cette URL "feed"
    path("feed/", feed_view, name="feed"),
    # Route pour la déconnexion, associe la vue logout_view et nomme cette URL "logout"
    path("logout/", views.logout_view, name="logout"),
]
