import csv
from django.core.management.base import BaseCommand

from player.constants import Position
from player.models import Player, PlayerPosition


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('adp_data.csv', 'rU') as f:
            reader = csv.reader(f)
            lines = list(reader)

        for l in lines:
            name = l[2]
            position = Position.from_canonical(lines[0][3])

            player = Player.objects.get_or_create(name=name)[0]
            PlayerPosition.objects.get_or_create(player=player, position=position)
