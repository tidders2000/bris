# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-24 22:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estab', '0012_auto_20191121_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='establishment',
            name='hours',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]
