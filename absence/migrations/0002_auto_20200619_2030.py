# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-19 20:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('absence', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='absence',
            name='reason',
        ),
        migrations.AddField(
            model_name='absence',
            name='reason',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='absence.Reason'),
        ),
    ]
