from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    bio = forms.CharField(widget=forms.Textarea, required=False, help_text="Tell us about yourself (optional).")

    class Meta:
        model = User
        fields = ("username", "email", "bio", "password1", "password2")


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
