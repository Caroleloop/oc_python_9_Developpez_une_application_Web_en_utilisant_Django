from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from accounts.models import UserFollows
from .models import Ticket, Review
from .forms import TicketForm, ReviewForm
from itertools import chain
from operator import attrgetter
from django.db import models


def feed_view(request):
    """
    Affiche le fil d'actualité pour l'utilisateur connecté.
    Ce fil regroupe les tickets et critiques des utilisateurs suivis ainsi que ceux de l'utilisateur lui-même,
    triés par date de création, du plus récent au plus ancien.

    Args:
        request (HttpRequest): La requête HTTP entrante.

    Returns:
        HttpResponse: La page 'feed.html' avec les éléments du fil d'actualité.
    """
    current_user = request.user
    followed_users = UserFollows.objects.filter(user=current_user).values_list("followed_user", flat=True)
    visible_users = list(followed_users) + [current_user.id]

    tickets = Ticket.objects.filter(user__in=visible_users)
    reviews = Review.objects.filter(models.Q(user__in=visible_users) | models.Q(ticket__in=tickets))

    feed_items = sorted(chain(tickets, reviews), key=attrgetter("time_created"), reverse=True)

    return render(request, "feed/feed.html", {"feed_items": feed_items})


@login_required
def add_ticket(request):
    """
    Permet à un utilisateur connecté de créer un nouveau ticket via un formulaire.

    Args:
        request (HttpRequest): La requête HTTP entrante.

    Returns:
        HttpResponse: Redirige vers le fil d'actualité en cas de succès, sinon réaffiche le formulaire.
    """
    form = TicketForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        ticket = form.save(commit=False)
        ticket.user = request.user
        ticket.save()
        return redirect("feed")

    return render(request, "feed/ticket_form.html", {"form": form})


@login_required
def edit_ticket(request, ticket_id):
    """
    Permet à l'auteur d'un ticket connecté d'éditer son ticket.

    Args:
        request (HttpRequest): La requête HTTP entrante.
        ticket_id (int): L'identifiant du ticket à modifier.

    Returns:
        HttpResponse: Redirige vers le fil d'actualité si succès, sinon affiche le formulaire d'édition.
        HttpResponseForbidden: Si l'utilisateur n'est pas l'auteur du ticket.
    """
    ticket = get_object_or_404(Ticket, id=ticket_id)

    if ticket.user != request.user:
        return HttpResponseForbidden()

    form = TicketForm(request.POST or None, request.FILES or None, instance=ticket)

    if form.is_valid():
        form.save()
        return redirect("feed")

    return render(request, "feed/ticket_form.html", {"form": form, "ticket": ticket})


@login_required
def delete_ticket(request, ticket_id):
    """
    Permet à l'auteur d'un ticket de le supprimer après confirmation.

    Args:
        request (HttpRequest): La requête HTTP entrante.
        ticket_id (int): L'identifiant du ticket à supprimer.

    Returns:
        HttpResponse: Redirige vers le fil d'actualité après suppression ou affiche la page de confirmation.
        HttpResponseForbidden: Si l'utilisateur n'est pas l'auteur du ticket.
    """
    ticket = get_object_or_404(Ticket, id=ticket_id)

    if ticket.user != request.user:
        return HttpResponseForbidden()

    if request.method == "POST":
        ticket.delete()
        return redirect("feed")

    return render(request, "feed/ticket_confirm_delete.html", {"ticket": ticket})


@login_required
def ticket_detail(request, ticket_id):
    """
    Affiche les détails d'un ticket ainsi que toutes ses critiques associées.

    Args:
        request (HttpRequest): La requête HTTP entrante.
        ticket_id (int): L'identifiant du ticket à afficher.

    Returns:
        HttpResponse: La page de détail du ticket avec ses critiques.
    """
    ticket = get_object_or_404(Ticket, id=ticket_id)
    reviews = ticket.reviews.all()
    return render(request, "feed/ticket_detail.html", {"ticket": ticket, "reviews": reviews})


@login_required
def add_review(request, ticket_id):
    """
    Permet d'ajouter une critique à un ticket donné, si aucune critique n'existe déjà pour ce ticket.

    Args:
        request (HttpRequest): La requête HTTP entrante.
        ticket_id (int): L'identifiant du ticket à critiquer.

    Returns:
        HttpResponse: Redirige vers le fil d'actualité ou vers le détail du ticket en cas d'erreur.
    """
    ticket = get_object_or_404(Ticket, id=ticket_id)

    existing_review = Review.objects.filter(ticket=ticket).first()
    if existing_review:
        from django.contrib import messages

        messages.error(request, "Ce ticket a déjà une critique, vous ne pouvez pas en créer une autre.")
        return redirect("ticket_detail", ticket_id=ticket.id)

    form = ReviewForm(request.POST or None)

    if form.is_valid():
        review = form.save(commit=False)
        review.user = request.user
        review.ticket = ticket
        review.save()
        return redirect("feed")

    return render(request, "feed/review_form.html", {"form": form, "ticket": ticket})


@login_required
def edit_review(request, review_id):
    """
    Permet à l'auteur d'une critique de la modifier.

    Args:
        request (HttpRequest): La requête HTTP entrante.
        review_id (int): L'identifiant de la critique à modifier.

    Returns:
        HttpResponse: Redirige vers le fil d'actualité ou affiche le formulaire d'édition.
        HttpResponseForbidden: Si l'utilisateur n'est pas l'auteur de la critique.
    """
    review = get_object_or_404(Review, id=review_id)

    if review.user != request.user:
        return HttpResponseForbidden()

    form = ReviewForm(request.POST or None, instance=review)

    if form.is_valid():
        form.save()
        return redirect("feed")

    return render(request, "feed/review_form.html", {"form": form, "ticket": review.ticket})


@login_required
def delete_review(request, review_id):
    """
    Permet à l'auteur d'une critique de la supprimer après confirmation.

    Args:
        request (HttpRequest): La requête HTTP entrante.
        review_id (int): L'identifiant de la critique à supprimer.

    Returns:
        HttpResponse: Redirige vers le fil d'actualité ou affiche la page de confirmation.
        HttpResponseForbidden: Si l'utilisateur n'est pas l'auteur de la critique.
    """
    review = get_object_or_404(Review, id=review_id)

    if review.user != request.user:
        return HttpResponseForbidden()

    if request.method == "POST":
        review.delete()
        return redirect("feed")

    return render(request, "feed/review_confirm_delete.html", {"review": review})


@login_required
def add_review_without_ticket(request):
    """
    Permet à un utilisateur connecté de créer simultanément un ticket et une critique associée.

    Args:
        request (HttpRequest): La requête HTTP entrante.

    Returns:
        HttpResponse: Redirige vers le fil d'actualité en cas de succès, sinon affiche les formulaires.
    """
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
        request,
        "feed/add_review_without_ticket.html",
        {"ticket_form": ticket_form, "review_form": review_form},
    )


@login_required
def my_posts_view(request):
    """
    Affiche les tickets et critiques créés par l'utilisateur connecté, triés par date décroissante.

    Args:
        request (HttpRequest): La requête HTTP entrante.

    Returns:
        HttpResponse: La page listant les publications de l'utilisateur.
    """
    user = request.user
    tickets = Ticket.objects.filter(user=user)
    reviews = Review.objects.filter(user=user)

    my_posts = sorted(chain(tickets, reviews), key=attrgetter("time_created"), reverse=True)

    return render(request, "feed/my_posts.html", {"my_posts": my_posts})
