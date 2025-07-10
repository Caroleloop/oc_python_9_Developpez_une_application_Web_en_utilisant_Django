from django.apps import AppConfig


class FeedConfig(AppConfig):
    """
    Configuration de l'application 'feed' pour Django.

    Cette classe hérite de AppConfig et permet de configurer certains
    paramètres spécifiques à l'application 'feed', comme le type de clé
    primaire par défaut pour les modèles et le nom de l'application.
    """

    # Définit le type de clé primaire auto-incrémentée par défaut pour les modèles
    # Cette configuration utilise un BigAutoField qui est un entier 64 bits,
    # ce qui est utile pour les bases de données avec beaucoup d'entrées.
    default_auto_field = "django.db.models.BigAutoField"

    # Nom interne de l'application dans le projet Django
    name = "feed"
