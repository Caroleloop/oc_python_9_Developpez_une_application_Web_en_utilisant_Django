from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # Classe qui hérite de AbstractUser pour créer un utilisateur personnalisé
    # Ajout d'un champ supplémentaire "bio" pour permettre aux utilisateurs d'ajouter une biographie
    bio = models.TextField(blank=True, null=True)  # Champ texte optionnel, peut être vide ou nul
    pass  # Indique qu'il n'y a pas d'autre ajout pour l'instant


class UserFollows(models.Model):
    # Modèle pour représenter la relation "suivre" entre utilisateurs (relation Many-to-Many via modèle intermédiaire)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    # Utilisateur qui suit quelqu'un
    # Si cet utilisateur est supprimé, toutes ses relations "follow" sont aussi supprimées
    # related_name "following" permet d'accéder aux utilisateurs suivis depuis un utilisateur

    followed_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followed_by")
    # Utilisateur qui est suivi
    # Si cet utilisateur est supprimé, les relations "followed" sont aussi supprimées
    # related_name "followed_by" permet d'accéder aux utilisateurs qui suivent cet utilisateur

    class Meta:
        unique_together = ("user", "followed_user")
        # Empêche qu'un utilisateur suive plusieurs fois la même personne (unicité de la paire)
        verbose_name = "Abonnement"  # Nom au singulier utilisé dans l’admin Django
        verbose_name_plural = "Abonnements"  # Nom au pluriel utilisé dans l’admin Django

    def __str__(self):
        # Représentation en chaîne de caractères du modèle, pratique pour l’affichage en admin ou logs
        return f"{self.user.username} suit {self.followed_user.username}"
