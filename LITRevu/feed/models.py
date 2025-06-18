from django.db import models
from django.conf import settings


class Ticket(models.Model):
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
        # Représentation textuelle du ticket, affichant le titre et le nom de l'utilisateur
        return f"Ticket: {self.title} par {self.user.username}"


class Review(models.Model):
    # Relation avec le ticket auquel la critique est associée, suppression en cascade
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)

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
        # Représentation textuelle de la critique, affichant l'utilisateur et le titre du ticket
        return f"Critique de {self.user.username} sur {self.ticket.title}"
