# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-03 14:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ntgame', '0027_auto_20170803_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='EffectInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('magnitude', models.FloatField()),
                ('effect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ntgame.Effect')),
            ],
        ),
        migrations.RenameField(
            model_name='building',
            old_name='diminishing_ratio',
            new_name='diminishing_return',
        ),
        migrations.AlterField(
            model_name='buildingeffectinstance',
            name='magnitude',
            field=models.FloatField(),
        ),
        migrations.AddField(
            model_name='building',
            name='effect_instance',
            field=models.ManyToManyField(to='ntgame.EffectInstance'),
        ),
    ]