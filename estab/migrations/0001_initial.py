# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-10 09:35
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
            name='Establishment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shiftname', models.CharField(default='shift', max_length=254)),
                ('team', models.CharField(choices=[('nurseing', 'nursing'), ('hca', 'hca'), ('admin', 'admin')], max_length=254)),
                ('location', models.CharField(choices=[('bingham', 'bingham'), ('cropwell', 'cropwell'), ('cotgrave', 'cotgrave')], default='bingham', max_length=254)),
                ('shift_start', models.TimeField()),
                ('shift_end', models.TimeField()),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')], max_length=254)),
                ('hours', models.DecimalField(decimal_places=1, default=0, max_digits=3)),
                ('allocated', models.BooleanField(default=False)),
                ('width', models.CharField(default='20', max_length=254)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
