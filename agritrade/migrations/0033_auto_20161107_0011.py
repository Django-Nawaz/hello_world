# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-06 18:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agritrade', '0032_auto_20161107_0003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin_comments',
            name='A_id',
        ),
        migrations.RemoveField(
            model_name='admin_comments',
            name='admin_id',
        ),
        migrations.RemoveField(
            model_name='buyer_comments',
            name='B_id',
        ),
        migrations.RemoveField(
            model_name='buyer_comments',
            name='Buyer_id',
        ),
        migrations.RemoveField(
            model_name='farmer_comments',
            name='F_id',
        ),
        migrations.RemoveField(
            model_name='farmer_comments',
            name='farmer_id',
        ),
        migrations.RemoveField(
            model_name='staff_comments',
            name='S_id',
        ),
        migrations.RemoveField(
            model_name='staff_comments',
            name='Staff_id',
        ),
        migrations.DeleteModel(
            name='Admin_Comments',
        ),
        migrations.DeleteModel(
            name='Buyer_Comments',
        ),
        migrations.DeleteModel(
            name='Farmer_Comments',
        ),
        migrations.DeleteModel(
            name='Staff_Comments',
        ),
    ]