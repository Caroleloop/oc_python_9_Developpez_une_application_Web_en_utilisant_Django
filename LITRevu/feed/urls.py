from django.urls import path
from .views import feed_view

urlpatterns = [
    # Définition d'une URL qui mappe la route 'feed/' à la vue 'feed_view'
    # Le nom 'feed' permet de référencer cette URL facilement ailleurs dans le projet
    path("feed/", feed_view, name="feed"),
]
