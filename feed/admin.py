from django.contrib import admin
from .models import Ticket, Review

"""
Module d'administration Django pour les modèles Ticket et Review.

Ce module enregistre les modèles dans l'interface d'administration Django,
permettant ainsi une gestion facile des tickets et des avis (reviews).
"""

# Enregistrement du modèle Ticket
# Ce modèle représente un ticket (par exemple, un problème ou une demande).
# En l'enregistrant ici, on peut créer, modifier et supprimer des tickets via l'administration Django.
admin.site.register(Ticket)

# Enregistrement du modèle Review
# Ce modèle représente une critique ou un avis associé à un ticket.
# Son enregistrement permet de gérer ces avis dans l'interface d'administration.
admin.site.register(Review)
