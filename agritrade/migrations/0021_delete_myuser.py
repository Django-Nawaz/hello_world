# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-19 12:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agritrade', '0020_myuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyUser',
        ),
    ]
