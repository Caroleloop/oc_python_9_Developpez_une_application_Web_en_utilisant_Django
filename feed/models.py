from django.db import models
from django.conf import settings


class Ticket(models.Model):
    """
    Modèle représentant un ticket soumis par un utilisateur.

    Attributs :
        title (CharField): Titre du ticket, texte court limité à 128 caractères.
        description (TextField): Description détaillée du ticket, champ optionnel.
        user (ForeignKey): Référence à l'utilisateur ayant créé le ticket.
        image (ImageField): Image associée au ticket, optionnelle.
        time_created (DateTimeField): Date et heure de création du ticket, définies automatiquement.
    """

    # Titre du ticket, chaîne de caractères avec une longueur maximale de 128 caractères
    title = models.CharField(max_length=128)

    # Description du ticket, champ texte pouvant être vide
    description = models.TextField(blank=True)

    # Relation avec l'utilisateur ayant créé le ticket, suppression en cascade si l'utilisateur est supprimé
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Image associée au ticket, optionnelle, enregistrée dans le dossier 'ticket_images/'
    image = models.ImageField(upload_to="ticket_images/", blank=True, null=True)

    # Date et heure de création du ticket, ajout automatique à la création
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Retourne une représentation textuelle du ticket.

        Format : "Ticket: <title> par <username>"
        """
        return f"Ticket: {self.title} par {self.user.username}"


class Review(models.Model):
    """
    Modèle représentant une critique associée à un ticket.

    Attributs :
        ticket (ForeignKey): Référence au ticket concerné.
        rating (PositiveSmallIntegerField): Note de 0 à 5.
        headline (CharField): Titre de la critique.
        body (TextField): Contenu détaillé de la critique, optionnel.
        user (ForeignKey): Utilisateur ayant écrit la critique.
        time_created (DateTimeField): Date et heure de création de la critique, définies automatiquement.
    """

    # Relation avec le ticket auquel la critique est associée, suppression en cascade
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="reviews")

    # Note donnée, entière positive entre 0 et 5 inclus, avec choix limités
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(0, 6)])

    # Titre de la critique, chaîne de caractères avec une longueur maximale de 128 caractères
    headline = models.CharField(max_length=128)

    # Contenu de la critique, champ texte pouvant être vide
    body = models.TextField(blank=True)

    # Relation avec l'utilisateur ayant écrit la critique, suppression en cascade si l'utilisateur est supprimé
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Date et heure de création de la critique, ajout automatique à la création
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Retourne une représentation textuelle de la critique.

        Format : "Critique de <username> sur <ticket_title>"
        """
        return f"Critique de {self.user.username} sur {self.ticket.title}"
