# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-03 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='months',
            name='finsh',
            field=models.CharField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='months',
            name='start',
            field=models.CharField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
