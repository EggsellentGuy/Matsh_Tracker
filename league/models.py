from django.db import models


# Create your models here.
class Player(models.Model):
    nickname = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nickname


class Match(models.Model):
    winner = models.ForeignKey(
        Player, on_delete=models.PROTECT, related_name="won_matches"
    )
    loser = models.ForeignKey(
        Player, on_delete=models.PROTECT, related_name="lost_matches"
    )
    played_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.winner} defeated {self.loser}"
