from django import forms
from .models import Ticket, Review


class TicketForm(forms.ModelForm):
    """
    Formulaire basé sur le modèle Ticket.

    Ce formulaire permet de créer ou modifier un ticket avec les champs :
    - title : le titre du ticket
    - description : la description détaillée du ticket
    - image : une image associée au ticket (optionnelle)
    """

    class Meta:
        model = Ticket  # Le modèle associé à ce formulaire
        fields = ["title", "description", "image"]  # Champs inclus dans le formulaire


class ReviewForm(forms.ModelForm):
    """
    Formulaire basé sur le modèle Review.

    Ce formulaire permet de créer ou modifier une revue avec les champs :
    - rating : la note attribuée (ex : sur 5 étoiles)
    - headline : le titre de la revue
    - body : le contenu détaillé de la revue
    """

    class Meta:
        model = Review  # Le modèle associé à ce formulaire
        fields = ["rating", "headline", "body"]  # Champs inclus dans le formulaire
