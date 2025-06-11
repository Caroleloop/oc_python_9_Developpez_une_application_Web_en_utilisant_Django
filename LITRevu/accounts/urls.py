from django.urls import path
from . import views


urlpatterns = [
    path("", views.dual_auth_view, name="login"),
    path("signup/", views.signup_view, name="signup"),
    path("feed/", views.feed_view, name="feed"),
    path("logout/", views.logout_view, name="logout"),
]
