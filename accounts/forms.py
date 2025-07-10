from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

# Récupère le modèle utilisateur actif (souvent un modèle User personnalisé)
User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    """
    Formulaire personnalisé pour la création d'un nouvel utilisateur.

    Ajoute un champ 'bio' facultatif permettant à l'utilisateur de se décrire.
    Hérite de UserCreationForm pour bénéficier des champs et validations par défaut.
    """

    bio = forms.CharField(
        widget=forms.Textarea,  # Affiche une zone de texte multilignes pour la bio
        required=False,  # Champ facultatif
        help_text="Tell us about yourself (optional).",  # Message d'aide à l'utilisateur
    )

    class Meta:
        """
        Configuration du formulaire.

        - model : modèle utilisateur lié à ce formulaire.
        - fields : liste des champs à afficher dans le formulaire.
        """

        model = User
        fields = ("username", "email", "bio", "password1", "password2")


class CustomAuthenticationForm(AuthenticationForm):
    """
    Formulaire personnalisé pour l'authentification (connexion) de l'utilisateur.

    Hérite d'AuthenticationForm, peut être personnalisé ultérieurement si besoin.
    """

    class Meta:
        """
        Configuration du formulaire.

        - model : modèle utilisateur lié à ce formulaire.
        """

        model = User


class FollowUserForm(forms.Form):
    """
    Formulaire simple pour permettre à un utilisateur de suivre un autre utilisateur.

    Contient un champ username pour saisir le nom d'utilisateur à suivre.
    """

    username = forms.CharField(
        label="Nom d'utilisateur à suivre",
        max_length=150,
    )

    def clean_username(self):
        """
        Valide que l'utilisateur avec ce nom existe bien dans la base de données.

        - Récupère l'objet utilisateur correspondant au nom donné.
        - Lève une ValidationError si l'utilisateur n'existe pas.

        Retourne l'objet User s'il est valide.
        """
        username = self.cleaned_data["username"]
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError("Cet utilisateur n'existe pas.")
        return user
