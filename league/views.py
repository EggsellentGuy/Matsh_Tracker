from django.shortcuts import render, redirect
from .forms import PlayerForm
from .models import Player


def player_list(request):
    players = Player.objects.all()
    return render(
        request,
        "league/player_list.html",
        context={"players": players},
    )


def player_create(request):
    if request.method == "POST":
        form = PlayerForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("player_list")

    else:
        form = PlayerForm()

    return render(
        request,
        "league/player_form.html",
        {"form": form},
    )
