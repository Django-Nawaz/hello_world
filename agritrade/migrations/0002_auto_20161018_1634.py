# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-18 11:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agritrade', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='pincode',
            field=models.IntegerField(),
        ),
    ]
