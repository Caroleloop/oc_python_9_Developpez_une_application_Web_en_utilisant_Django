from django.apps import AppConfig


# Définition de la configuration de l'application 'accounts'
class AccountsConfig(AppConfig):
    # Spécifie le type de champ utilisé par défaut pour les clés primaires dans les modèles
    default_auto_field = "django.db.models.BigAutoField"

    # Nom de l'application Django
    name = "accounts"
