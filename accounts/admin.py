from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserFollows

"""
Module d'administration Django pour les modèles personnalisés User et UserFollows.

Ce module enregistre les modèles dans l'interface d'administration Django,
permettant ainsi une gestion facile des utilisateurs et de leurs relations de suivi.
"""

# Enregistrement du modèle User avec les fonctionnalités avancées de UserAdmin
# UserAdmin fournit une interface d'administration complète pour la gestion des utilisateurs,
# incluant la gestion des permissions, groupes, et autres attributs spécifiques.
admin.site.register(User, UserAdmin)

# Enregistrement du modèle UserFollows
# Ce modèle représente les relations de suivi entre utilisateurs (qui suit qui).
# En l'enregistrant ici, on peut gérer ces relations directement via l'administration Django.
admin.site.register(UserFollows)
