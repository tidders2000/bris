# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-19 14:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(choices=[('nurseing', 'nursing'), ('hca', 'hca'), ('admin', 'admin')], max_length=254)),
                ('location', models.CharField(choices=[('bingham', 'bingham'), ('cropwell', 'cropwell'), ('cotgrave', 'cotgrave')], default='bingham', max_length=254)),
                ('date_start', models.TimeField()),
                ('date_end', models.TimeField()),
                ('approved', models.BooleanField(default=False)),
                ('days', models.CharField(max_length=254)),
                ('appmanager', models.CharField(max_length=254, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
