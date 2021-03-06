# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-30 23:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user_rank',
        ),
        migrations.AddField(
            model_name='profile',
            name='position',
            field=models.CharField(choices=[('UG', 'Under graduate'), ('MSc', 'MSC student'), ('PhD', 'PhD student'), ('RA/RF', 'Postdocs'), ('PI', 'PI'), ('Other', 'Other')], default='Other', max_length=10),
        ),
    ]
