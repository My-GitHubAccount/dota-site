# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game_log', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='dire_hero_1',
            field=models.TextField(choices=[('LESH', 'Leshrac'), ('PA', 'Phantom Assasin'), ('SF', 'Shadow Fiend')]),
        ),
        migrations.AlterField(
            model_name='game',
            name='dire_hero_2',
            field=models.TextField(choices=[('LESH', 'Leshrac'), ('PA', 'Phantom Assasin'), ('SF', 'Shadow Fiend')]),
        ),
        migrations.AlterField(
            model_name='game',
            name='dire_hero_3',
            field=models.TextField(choices=[('LESH', 'Leshrac'), ('PA', 'Phantom Assasin'), ('SF', 'Shadow Fiend')]),
        ),
        migrations.AlterField(
            model_name='game',
            name='dire_hero_4',
            field=models.TextField(choices=[('LESH', 'Leshrac'), ('PA', 'Phantom Assasin'), ('SF', 'Shadow Fiend')]),
        ),
        migrations.AlterField(
            model_name='game',
            name='dire_hero_5',
            field=models.TextField(choices=[('LESH', 'Leshrac'), ('PA', 'Phantom Assasin'), ('SF', 'Shadow Fiend')]),
        ),
        migrations.AlterField(
            model_name='game',
            name='radient_hero_1',
            field=models.TextField(choices=[('LESH', 'Leshrac'), ('PA', 'Phantom Assasin'), ('SF', 'Shadow Fiend')]),
        ),
        migrations.AlterField(
            model_name='game',
            name='radient_hero_2',
            field=models.TextField(choices=[('LESH', 'Leshrac'), ('PA', 'Phantom Assasin'), ('SF', 'Shadow Fiend')]),
        ),
        migrations.AlterField(
            model_name='game',
            name='radient_hero_3',
            field=models.TextField(choices=[('LESH', 'Leshrac'), ('PA', 'Phantom Assasin'), ('SF', 'Shadow Fiend')]),
        ),
        migrations.AlterField(
            model_name='game',
            name='radient_hero_4',
            field=models.TextField(choices=[('LESH', 'Leshrac'), ('PA', 'Phantom Assasin'), ('SF', 'Shadow Fiend')]),
        ),
        migrations.AlterField(
            model_name='game',
            name='radient_hero_5',
            field=models.TextField(choices=[('LESH', 'Leshrac'), ('PA', 'Phantom Assasin'), ('SF', 'Shadow Fiend')]),
        ),
    ]
