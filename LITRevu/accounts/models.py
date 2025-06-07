from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # champs personnalisés :
    bio = models.TextField(blank=True, null=True)
    pass
