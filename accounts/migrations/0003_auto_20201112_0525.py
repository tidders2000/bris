# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-12 05:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200205_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='team',
            field=models.CharField(choices=[('nurseing', 'nursing'), ('hca', 'hca'), ('admin', 'admin'), ('admin_CB', 'admin_CB'), ('admin_COT', 'admin_COT'), ('Dispensary', 'Dispensary'), ('admin_BIN', 'admin_BIN')], max_length=254),
        ),
    ]