# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_played', models.DateField()),
                ('game', models.TextField()),
                ('radient', models.TextField()),
                ('dire', models.TextField()),
                ('first_pick', models.TextField()),
                ('team_victory', models.TextField()),
                ('dire_hero_1', models.TextField()),
                ('dire_hero_2', models.TextField()),
                ('dire_hero_3', models.TextField()),
                ('dire_hero_4', models.TextField()),
                ('dire_hero_5', models.TextField()),
                ('radient_hero_1', models.TextField()),
                ('radient_hero_2', models.TextField()),
                ('radient_hero_3', models.TextField()),
                ('radient_hero_4', models.TextField()),
                ('radient_hero_5', models.TextField()),
            ],
        ),
    ]
