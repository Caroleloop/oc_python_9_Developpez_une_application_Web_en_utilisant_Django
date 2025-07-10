from django.urls import path
from .views import feed_view
from . import views

# Liste des patterns d'URLs pour l'application
urlpatterns = [
    # URL principale de l'application affichant le flux principal (feed)
    # Exemple d'URL : "/"
    path("", feed_view, name="feed"),
    # URL pour ajouter un nouveau ticket
    # Exemple d'URL : "/ticket/add/"
    path("ticket/add/", views.add_ticket, name="add_ticket"),
    # URL pour éditer un ticket existant identifié par son ID
    # Exemple d'URL : "/ticket/5/edit/"
    path("ticket/<int:ticket_id>/edit/", views.edit_ticket, name="edit_ticket"),
    # URL pour supprimer un ticket existant identifié par son ID
    # Exemple d'URL : "/ticket/5/delete/"
    path("ticket/<int:ticket_id>/delete/", views.delete_ticket, name="delete_ticket"),
    # URL pour afficher les détails d'un ticket identifié par son ID
    # Exemple d'URL : "/ticket/5/"
    path("ticket/<int:ticket_id>/", views.ticket_detail, name="ticket_detail"),
    # URL pour ajouter un avis (review) à un ticket identifié par son ID
    # Exemple d'URL : "/review/5/add/"
    path("review/<int:ticket_id>/add/", views.add_review, name="add_review"),
    # URL pour éditer un avis identifié par son ID
    # Exemple d'URL : "/review/7/edit/"
    path("review/<int:review_id>/edit/", views.edit_review, name="edit_review"),
    # URL pour supprimer un avis identifié par son ID
    # Exemple d'URL : "/review/7/delete/"
    path("review/<int:review_id>/delete/", views.delete_review, name="delete_review"),
    # URL pour ajouter un avis sans ticket associé
    # Exemple d'URL : "/reviews/add/"
    path("reviews/add/", views.add_review_without_ticket, name="add_review_without_ticket"),
    # URL pour afficher les publications de l'utilisateur connecté
    # Exemple d'URL : "/my-posts/"
    path("my-posts/", views.my_posts_view, name="my_posts"),
]
