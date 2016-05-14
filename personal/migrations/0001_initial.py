# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-14 13:00
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
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
            ],
            options={
                'verbose_name_plural': 'Groups',
                'verbose_name': 'Group',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Teacher', 'Teacher'), ('Student', 'Student'), ('Stranger', 'Stranger')], max_length=30)),
                ('avatar', models.ImageField(blank=True, upload_to='avatar/', verbose_name='avatar')),
            ],
        ),
        migrations.CreateModel(
            name='StudentCard',
            fields=[
                ('card_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.Group')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='student_info',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='personal.StudentCard'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='group',
            name='teachers',
            field=models.ManyToManyField(to='personal.Profile'),
        ),
    ]
