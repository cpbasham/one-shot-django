# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=64)),
                ('map', models.CharField(default=b'any', max_length=4, choices=[(b'any', b'Any Map'), (b'SR', b"Summoner's Rift"), (b'TT', b'Twisted Treeline'), (b'HA', b'Howling Abyss'), (b'CS', b'Crystal Scar')])),
                ('game_type', models.CharField(default=b'any', max_length=8, choices=[(b'any', b'Any Mode'), (b'CLASSIC', b'Classic'), (b'ARAM', b'ARAM'), (b'ODIN', b'Dominion')])),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
                'verbose_name': 'ItemSet',
                'verbose_name_plural': 'ItemSets',
            },
        ),
    ]
