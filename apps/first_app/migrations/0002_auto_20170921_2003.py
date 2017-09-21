# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-21 20:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='messages',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='first_app.Message'),
        ),
    ]