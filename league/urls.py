from django.urls import path

from . import views

urlpatterns = [
    path("players/", views.player_list, name="player_list"),
    path("players/add/", views.player_create, name="player_create"),
]
