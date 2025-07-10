"""
ASGI config for LITRevu project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# Définit la variable d'environnement pour indiquer le module de configuration des settings Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LITRevu.settings")

# Récupère l'application ASGI Django, qui servira de point d'entrée pour le serveur ASGI
application = get_asgi_application()
