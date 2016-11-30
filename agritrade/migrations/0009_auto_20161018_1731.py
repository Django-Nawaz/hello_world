# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-18 12:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agritrade', '0008_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crop',
            name='Season',
            field=models.CharField(choices=[('SNY', 'Sunny'), ('WTR', 'Winter'), ('RNY', 'Rainy'), ('SPR', 'Spring')], max_length=50),
        ),
    ]
