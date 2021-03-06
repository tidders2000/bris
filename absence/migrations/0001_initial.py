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
            name='Absence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager', models.CharField(default='approver', max_length=254, null=True)),
                ('absence_start', models.DateField(null=True)),
                ('absence_end', models.DateField(blank=True, null=True)),
                ('gp_consult', models.BooleanField(default=False)),
                ('further_support', models.TextField(blank=True, null=True)),
                ('days', models.CharField(default=0, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Reason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='absence',
            name='reason',
            field=models.ManyToManyField(blank=True, null=True, to='absence.Reason'),
        ),
        migrations.AddField(
            model_name='absence',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
