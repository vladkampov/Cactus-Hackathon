# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-15 11:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0004_auto_20160515_0838'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistics',
            name='max_time',
            field=models.IntegerField(default=0),
        ),
    ]
