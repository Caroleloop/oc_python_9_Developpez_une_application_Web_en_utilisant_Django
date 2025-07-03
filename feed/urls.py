from django.urls import path
from .views import feed_view
from . import views

urlpatterns = [
    # Définition d'une URL qui mappe la route 'feed/' à la vue 'feed_view'
    # Le nom 'feed' permet de référencer cette URL facilement ailleurs dans le projet
    path("", feed_view, name="feed"),
    path("ticket/add/", views.add_ticket, name="add_ticket"),
    path("ticket/<int:ticket_id>/edit/", views.edit_ticket, name="edit_ticket"),
    path("ticket/<int:ticket_id>/delete/", views.delete_ticket, name="delete_ticket"),
    path("ticket/<int:ticket_id>/", views.ticket_detail, name="ticket_detail"),
    path("review/<int:ticket_id>/add/", views.add_review, name="add_review"),
    path("review/<int:review_id>/edit/", views.edit_review, name="edit_review"),
    path("review/<int:review_id>/delete/", views.delete_review, name="delete_review"),
    path("reviews/add/", views.add_review_without_ticket, name="add_review_without_ticket"),
]
