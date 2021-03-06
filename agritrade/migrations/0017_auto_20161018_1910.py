# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-18 13:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agritrade', '0016_auto_20161018_1838'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer_Phones',
            fields=[
                ('phone_id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('phone', models.BigIntegerField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Farmer_Phones',
            fields=[
                ('phone_id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('phone', models.BigIntegerField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Staff_Phones',
            fields=[
                ('phone_id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('phone', models.BigIntegerField(default=None)),
            ],
        ),
        migrations.RemoveField(
            model_name='phones',
            name='id',
        ),
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='staff',
            name='phone',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='buyer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='agritrade.Customer'),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='phone',
            field=models.IntegerField(default=None),
        ),
        migrations.DeleteModel(
            name='Phones',
        ),
        migrations.AddField(
            model_name='staff_phones',
            name='id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agritrade.Staff'),
        ),
        migrations.AddField(
            model_name='farmer_phones',
            name='id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agritrade.Farmer'),
        ),
        migrations.AddField(
            model_name='buyer_phones',
            name='id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agritrade.Buyer'),
        ),
    ]
