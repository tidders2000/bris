# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-26 21:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estab', '0006_auto_20200626_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='shifts',
            name='Monday',
            field=models.CharField(default='08:00-17:00', max_length=254),
        ),
        migrations.AddField(
            model_name='shifts',
            name='Monday_hours',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='shifts',
            name='Tuesday',
            field=models.CharField(default='08:00-17:00', max_length=254),
        ),
        migrations.AddField(
            model_name='shifts',
            name='Tuesday_hours',
            field=models.IntegerField(default=0),
        ),
    ]
