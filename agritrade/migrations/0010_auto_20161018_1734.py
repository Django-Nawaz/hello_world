# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-18 12:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agritrade', '0009_auto_20161018_1731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crop',
            name='Weather',
        ),
        migrations.AlterField(
            model_name='crop',
            name='Soil_health',
            field=models.CharField(choices=[(1, 'Excellent'), (2, 'Very Good'), (3, 'Good'), (4, 'Satisfactory'), (5, 'Bad')], max_length=50),
        ),
    ]
