from django.shortcuts import render, redirect
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
        nickname = request.POST.get("nickname", "").strip()
        if not nickname:
            return render(
                request,
                "league/player_form.html",
                context={"error": "Nickname cannot be empty"},
            )
        if Player.objects.filter(nickname=nickname).exists():
            return render(
                request,
                "league/player_form.html",
                context={"error": "Nickname is already used"},
            )
        Player.objects.create(nickname=nickname)
        return redirect("player_list")

    return render(
        request,
        "league/player_form.html",
        context={},
    )
