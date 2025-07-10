from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Modèle personnalisé d'utilisateur héritant de AbstractUser.

    Ajoute un champ supplémentaire 'bio' permettant aux utilisateurs
    d'ajouter une biographie personnelle.
    """

    bio = models.TextField(blank=True, null=True)
    # Champ texte optionnel pouvant être vide ou nul

    pass


class UserFollows(models.Model):
    """
    Modèle intermédiaire représentant une relation de "suivi" entre utilisateurs.

    Permet de modéliser une relation Many-to-Many personnalisée
    entre utilisateurs via deux ForeignKey pointant vers User.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    """
    Utilisateur qui suit un autre utilisateur.

    La suppression de cet utilisateur supprime aussi ses relations de suivi.
    L'attribut 'related_name' permet d'accéder aux utilisateurs suivis via user.following.
    """

    followed_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followed_by")
    """
    Utilisateur suivi.

    La suppression de cet utilisateur supprime les relations où il est suivi.
    L'attribut 'related_name' permet d'accéder aux abonnés via user.followed_by.
    """

    class Meta:
        unique_together = ("user", "followed_user")
        # Empêche un doublon : un utilisateur ne peut suivre plusieurs fois la même personne

        verbose_name = "Abonnement"
        verbose_name_plural = "Abonnements"
        # Noms personnalisés pour l'administration Django

    def __str__(self):
        """
        Représentation textuelle de la relation de suivi.

        Utile pour l'affichage en interface admin ou lors de logs.
        """
        return f"{self.user.username} suit {self.followed_user.username}"
