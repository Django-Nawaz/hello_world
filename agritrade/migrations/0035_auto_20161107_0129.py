# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-06 19:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agritrade', '0034_auto_20161107_0124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crop_order',
            name='rate',
        ),
        migrations.RemoveField(
            model_name='crop_order',
            name='crop_for_sale',
        ),
        migrations.AddField(
            model_name='crop_order',
            name='crop_for_sale',
            field=models.ManyToManyField(to='agritrade.Crop'),
        ),
    ]
