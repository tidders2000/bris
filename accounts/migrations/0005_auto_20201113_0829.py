# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-13 08:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20201113_0821'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='ni_Number',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
