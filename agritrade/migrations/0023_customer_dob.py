# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-19 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agritrade', '0022_myuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]
