from django.db import models


# Create your models here.
class Player(models.Model):
    nickname = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nickname
