# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import player.constants
import django_richenum.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerPosition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', django_richenum.models.fields.IndexEnumField(player.constants.Position)),
                ('player', models.ForeignKey(to='player.Player')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='playerposition',
            unique_together=set([('player', 'position')]),
        ),
    ]
