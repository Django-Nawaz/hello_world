# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-18 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agritrade', '0007_auto_20161018_1712'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('staff_name', models.CharField(max_length=20)),
                ('Address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=20)),
                ('pincode', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Date of Joining', models.DateField(auto_now=True)),
                ('Date of Birth', models.DateField()),
                ('staff_type', models.CharField(max_length=200)),
                ('Access_level', models.IntegerField()),
                
            ],
        ),
    ]
