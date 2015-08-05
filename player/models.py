from django.db import models
from django_richenum.models import IndexEnumField

from player.constants import Position


class Player(models.Model):
    name = models.CharField(max_length=200, unique=True)


class PlayerPosition(models.Model):
    player = models.ForeignKey(Player)
    position = IndexEnumField(Position)

    class Meta:
        unique_together = ("player", "position")
