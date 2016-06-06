# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-30 01:45
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Raw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('harvester', models.CharField(max_length=200)),
                ('date_harvested', models.DateTimeField(verbose_name='date harvested')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]