# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-06 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='pot',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
            preserve_default=False,
        ),
    ]