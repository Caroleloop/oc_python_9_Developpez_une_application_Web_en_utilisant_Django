from django.contrib import admin
from .models import Ticket, Review

# Enregistrement du modèle Ticket dans l'interface d'administration
admin.site.register(Ticket)

# Enregistrement du modèle Review dans l'interface d'administration
admin.site.register(Review)
