# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-06 20:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agritrade', '0035_auto_20161107_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Customer Id'),
        ),
    ]