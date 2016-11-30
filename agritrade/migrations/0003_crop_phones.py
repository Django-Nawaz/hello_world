# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-18 11:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agritrade', '0002_auto_20161018_1634'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('crop_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('photograph', models.ImageField(height_field=200, upload_to='', width_field=200)),
                ('crop_desc', models.TextField(max_length=500)),
                ('crop_name', models.CharField(max_length=50)),
                ('seed', models.CharField(max_length=50)),
                ('Season', models.CharField(max_length=50)),
                ('fertilizer', models.CharField(max_length=50)),
                ('pesticides', models.CharField(max_length=50)),
                ('Irrigation', models.BooleanField()),
                ('Weather', models.CharField(max_length=50)),
                ('Soil_health', models.CharField(max_length=50)),
                ('Precaution', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Phones',
            fields=[
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='agritrade.Customer')),
                ('phone', models.BigIntegerField(max_length=10)),
            ],
        ),
    ]