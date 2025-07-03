from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from accounts.models import UserFollows
from .models import Ticket, Review
from .forms import TicketForm, ReviewForm
from itertools import chain
from operator import attrgetter


# VUE DU FIL D'ACTUALITÉ
def feed_view(request):
    # Cette vue gère la requête HTTP et retourne la page "feed.html" située dans le dossier "feed"
    current_user = request.user

    # Récupérer les utilisateurs suivis
    followed_users = UserFollows.objects.filter(user=current_user).values_list("followed_user", flat=True)

    # Inclure l'utilisateur courant dans les auteurs à afficher
    visible_users = list(followed_users) + [current_user.id]

    # Récupérer les tickets et critiques des utilisateurs visibles
    tickets = Ticket.objects.filter(user__in=visible_users)
    reviews = Review.objects.filter(user__in=visible_users)

    # Fusionner et trier par date de création (plus récent en premier)
    feed_items = sorted(chain(tickets, reviews), key=attrgetter("time_created"), reverse=True)

    return render(request, "feed/feed.html", {"feed_items": feed_items})


# VUES POUR LES TICKETS
@login_required
def add_ticket(request):
    # Initialise un formulaire de ticket, vide ou pré-rempli si POST
    form = TicketForm(request.POST or None, request.FILES or None)

    # Si le formulaire est valide, crée et enregistre un ticket
    if form.is_valid():
        ticket = form.save(commit=False)
        ticket.user = request.user  # Attribue l'utilisateur courant
        ticket.save()
        return redirect("feed")  # Redirige vers le fil d'actualité

    # Affiche le formulaire de création de ticket
    return render(request, "feed/ticket_form.html", {"form": form})


@login_required
def edit_ticket(request, ticket_id):
    # Récupère le ticket à modifier ou affiche une erreur 404 s'il n'existe pas
    ticket = get_object_or_404(Ticket, id=ticket_id)

    # Vérifie que l'utilisateur courant est bien l'auteur du ticket
    if ticket.user != request.user:
        return HttpResponseForbidden()

    # Initialise le formulaire avec les données existantes du ticket
    form = TicketForm(request.POST or None, request.FILES or None, instance=ticket)

    # Si le formulaire est valide, enregistre les modifications
    if form.is_valid():
        form.save()
        return redirect("feed")

    # Affiche le formulaire de modification
    return render(request, "feed/ticket_form.html", {"form": form, "ticket": ticket})


@login_required
def delete_ticket(request, ticket_id):
    # Récupère le ticket à supprimer ou affiche une erreur 404
    ticket = get_object_or_404(Ticket, id=ticket_id)

    # Vérifie que l'utilisateur courant est bien l'auteur
    if ticket.user != request.user:
        return HttpResponseForbidden()

    # Si méthode POST, supprime le ticket et redirige
    if request.method == "POST":
        ticket.delete()
        return redirect("feed")

    # Sinon, affiche la page de confirmation
    return render(request, "feed/ticket_confirm_delete.html", {"ticket": ticket})


@login_required
def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    reviews = ticket.review_set.all()  # récupère toutes les critiques associées
    return render(request, "feed/ticket_detail.html", {"ticket": ticket, "reviews": reviews})


# VUES POUR LES REVIEWS
@login_required
def add_review(request, ticket_id):
    # Récupère le ticket associé à la critique
    ticket = get_object_or_404(Ticket, id=ticket_id)

    # Initialise un formulaire de critique
    form = ReviewForm(request.POST or None)

    # Si le formulaire est valide, crée et enregistre une critique
    if form.is_valid():
        review = form.save(commit=False)
        review.user = request.user
        review.ticket = ticket  # Associe la critique au ticket
        review.save()
        return redirect("feed")

    # Affiche le formulaire de création de critique
    return render(request, "feed/review_form.html", {"form": form, "ticket": ticket})


@login_required
def edit_review(request, review_id):
    # Récupère la critique à modifier
    review = get_object_or_404(Review, id=review_id)

    # Vérifie que l'utilisateur courant est l'auteur
    if review.user != request.user:
        return HttpResponseForbidden()

    # Initialise le formulaire avec les données existantes
    form = ReviewForm(request.POST or None, instance=review)

    # Si le formulaire est valide, enregistre les modifications
    if form.is_valid():
        form.save()
        return redirect("feed")

    # Affiche le formulaire de modification
    return render(request, "feed/review_form.html", {"form": form, "ticket": review.ticket})


@login_required
def delete_review(request, review_id):
    # Récupère la critique à supprimer
    review = get_object_or_404(Review, id=review_id)

    # Vérifie que l'utilisateur est bien l'auteur
    if review.user != request.user:
        return HttpResponseForbidden()

    # Si méthode POST, supprime la critique et redirige
    if request.method == "POST":
        review.delete()
        return redirect("feed")

    # Affiche la page de confirmation
    return render(request, "feed/review_confirm_delete.html", {"review": review})


@login_required
def add_review_without_ticket(request):
    ticket_form = TicketForm(request.POST or None, request.FILES or None)
    review_form = ReviewForm(request.POST or None)

    if request.method == "POST":
        if ticket_form.is_valid() and review_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()

            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()

            return redirect("feed")

    return render(
        request, "feed/add_review_without_ticket.html", {"ticket_form": ticket_form, "review_form": review_form}
    )
