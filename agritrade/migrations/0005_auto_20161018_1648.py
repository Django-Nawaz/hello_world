# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-18 11:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agritrade', '0004_farmer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='phone',
            field=models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, to='agritrade.Phones', unique=True),
        ),
    ]