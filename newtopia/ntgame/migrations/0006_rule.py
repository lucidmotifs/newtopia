# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-01 00:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ntgame', '0005_delete_rule'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=40)),
                ('value', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]
