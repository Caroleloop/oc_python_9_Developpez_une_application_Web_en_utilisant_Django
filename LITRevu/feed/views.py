from django.shortcuts import render


def feed_view(request):
    # Cette vue gère la requête HTTP et retourne la page "feed.html" située dans le dossier "feed"
    return render(request, "feed/feed.html")
