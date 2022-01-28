# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-27 09:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_students'),
        ('attendance', '0010_auto_20180227_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateField()),
                ('hour1', models.IntegerField(default=0)),
                ('hour2', models.IntegerField(default=0)),
                ('hour3', models.IntegerField(default=0)),
                ('hour4', models.IntegerField(default=0)),
                ('hour5', models.IntegerField(default=0)),
                ('hour6', models.IntegerField(default=0)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Students')),
            ],
        ),
    ]
