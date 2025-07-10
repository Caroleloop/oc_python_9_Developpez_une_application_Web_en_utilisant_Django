from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """
    Configuration de l'application 'accounts' pour Django.

    Attributs :
        default_auto_field (str): Type de champ utilisé par défaut pour les clés primaires dans les modèles.
        name (str): Nom de l'application.
    """

    # Type de champ par défaut pour les clés primaires dans les modèles de cette application
    default_auto_field = "django.db.models.BigAutoField"

    # Nom de l'application Django tel qu'il apparaît dans INSTALLED_APPS
    name = "accounts"
