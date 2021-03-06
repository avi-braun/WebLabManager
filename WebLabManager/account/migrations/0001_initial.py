# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-30 22:29
from __future__ import unicode_literals

import datetime
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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('supervisor', models.CharField(max_length=30)),
                ('user_type', models.CharField(choices=[('U', 'User'), ('A', 'Lab admin')], default='Non Active', max_length=10)),
                ('user_rank', models.CharField(choices=[('UG', 'Under graduate'), ('MSc', 'MSC student'), ('PhD', 'PhD student'), ('Staff', 'Staff'), ('Other', 'Other')], default='Other', max_length=10)),
                ('CID', models.IntegerField(blank=True, null=True)),
                ('join_date', models.DateField(default=datetime.date(1977, 7, 25))),
                ('status', models.CharField(choices=[('NA', 'Non Active'), ('Active', 'Active'), ('New User', 'New')], default='Active', max_length=8)),
                ('description', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
