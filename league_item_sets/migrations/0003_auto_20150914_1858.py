# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('league_item_sets', '0002_itemrow'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('api_id', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='itemrow',
            old_name='item_set',
            new_name='parent_set',
        ),
        migrations.AddField(
            model_name='item',
            name='parent_row',
            field=models.ForeignKey(to='league_item_sets.ItemRow'),
        ),
    ]
