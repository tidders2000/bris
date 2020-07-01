# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-24 17:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estab', '0002_shifts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shifts',
            name='day',
        ),
        migrations.RemoveField(
            model_name='shifts',
            name='hours',
        ),
        migrations.RemoveField(
            model_name='shifts',
            name='shift_end',
        ),
        migrations.RemoveField(
            model_name='shifts',
            name='shift_start',
        ),
        migrations.RemoveField(
            model_name='shifts',
            name='user',
        ),
        migrations.AddField(
            model_name='shifts',
            name='shiftname',
            field=models.CharField(default='shift', max_length=254),
        ),
    ]
