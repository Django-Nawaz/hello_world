# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-05 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agritrade', '0027_auto_20161105_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crop',
            name='Soil_health',
            field=models.CharField(choices=[('EXe', 'Excellent'), (2, 'Very Good'), (3, 'Good'), (4, 'Satisfactory'), (5, 'Bad')], max_length=50),
        ),
    ]