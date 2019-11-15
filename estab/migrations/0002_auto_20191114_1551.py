# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-14 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estab', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='establishment',
            name='shiftname',
            field=models.CharField(default='shift', max_length=254),
        ),
        migrations.AlterField(
            model_name='establishment',
            name='hours',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
    ]
