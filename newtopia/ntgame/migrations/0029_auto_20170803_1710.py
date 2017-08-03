# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-03 15:10
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ntgame', '0028_auto_20170803_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('description', models.CharField(max_length=200)),
                ('variable_range', models.IntegerField(default=0)),
                ('difficulty', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)])),
                ('effect_instance', models.ManyToManyField(to='ntgame.EffectInstance')),
            ],
        ),
        migrations.RemoveField(
            model_name='effectapplication',
            name='building_effecti',
        ),
        migrations.AddField(
            model_name='effectapplication',
            name='instance',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ntgame.EffectInstance'),
        ),
    ]