# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-04-07 12:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ntgame', '0011_auto_20170407_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='province',
            name='military',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='ntgame.Military'),
            preserve_default=False,
        ),
    ]
