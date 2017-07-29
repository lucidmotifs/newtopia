# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-28 22:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ntgame', '0022_effect_etype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.RemoveField(
            model_name='building',
            name='effect',
        ),
        migrations.AddField(
            model_name='building',
            name='effect',
            field=models.ManyToManyField(to='ntgame.Effect'),
        ),
    ]
