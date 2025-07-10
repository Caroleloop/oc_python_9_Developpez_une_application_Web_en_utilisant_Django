"""
WSGI config for LITRevu project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Définit la variable d'environnement indiquant le fichier de configuration des settings Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LITRevu.settings")

# Crée et récupère l'application WSGI Django, qui sera le point d'entrée pour le serveur WSGI
application = get_wsgi_application()
