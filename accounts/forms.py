from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

# Récupère le modèle utilisateur actif (souvent 'User' personnalisé)
User = get_user_model()


# Formulaire personnalisé pour la création d'un utilisateur
class CustomUserCreationForm(UserCreationForm):
    # Ajout d'un champ bio facultatif avec une zone de texte
    bio = forms.CharField(
        widget=forms.Textarea,  # Champ affiché sous forme de zone de texte multilignes
        required=False,  # Champ non obligatoire
        help_text="Tell us about yourself (optional).",  # Message d'aide affiché à l'utilisateur
    )

    class Meta:
        # Indique le modèle sur lequel ce formulaire se base
        model = User
        # Champs à afficher dans le formulaire de création
        fields = ("username", "email", "bio", "password1", "password2")


# Formulaire personnalisé pour l'authentification (connexion) de l'utilisateur
class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        # Indique le modèle utilisateur lié à ce formulaire
        model = User


class FollowUserForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur à suivre", max_length=150)

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError("Cet utilisateur n'existe pas.")
        return user
