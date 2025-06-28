from django.apps import AppConfig


# Classe de configuration pour l'application 'feed'
class FeedConfig(AppConfig):
    # Spécifie le type de clé primaire auto-incrémentée par défaut pour les modèles de cette app
    default_auto_field = "django.db.models.BigAutoField"
    # Nom de l'application tel qu'il sera utilisé dans Django
    name = "feed"
