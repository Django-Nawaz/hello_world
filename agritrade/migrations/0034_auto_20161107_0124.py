# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-06 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agritrade', '0033_auto_20161107_0011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_process',
            name='Order_id',
        ),
        migrations.AddField(
            model_name='order_process',
            name='Order_id',
            field=models.ManyToManyField(to='agritrade.Crop_order'),
        ),
    ]
