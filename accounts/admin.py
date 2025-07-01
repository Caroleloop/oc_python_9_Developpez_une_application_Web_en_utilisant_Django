from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserFollows

# Enregistrement du modèle User dans l'administration Django

# On utilise UserAdmin pour bénéficier des fonctionnalités avancées de gestion des utilisateurs
admin.site.register(User, UserAdmin)

# Cela permet de gérer les relations de suivi entre utilisateurs via l'interface d'administration
admin.site.register(UserFollows)
