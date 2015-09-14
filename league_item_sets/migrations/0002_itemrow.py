# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('league_item_sets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemRow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=64)),
                ('item_set', models.ForeignKey(to='league_item_sets.ItemSet')),
            ],
        ),
    ]
