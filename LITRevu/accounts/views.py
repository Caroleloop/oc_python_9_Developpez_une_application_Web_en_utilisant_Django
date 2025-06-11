from django.contrib.auth import login
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.shortcuts import render, redirect


def dual_auth_view(request):
    login_form = CustomAuthenticationForm()
    if request.method == "POST":
        login_form = CustomAuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect("feed")
        else:
            print(login_form.errors)
    return render(
        request,
        "accounts/home.html",
        {
            "login_form": login_form,
        },
    )


def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("feed")
    else:
        form = CustomUserCreationForm()

    return render(request, "accounts/signup.html", {"form": form})


def feed_view(request):
    return render(request, "feed/feed.html")
