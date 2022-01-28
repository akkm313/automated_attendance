# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-27 08:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0004_record_hour'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='date_time',
        ),
        migrations.RemoveField(
            model_name='record',
            name='hour',
        ),
        migrations.AddField(
            model_name='record',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='hour1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='record',
            name='hour2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='record',
            name='hour3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='record',
            name='hour4',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='record',
            name='hour5',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='record',
            name='hour6',
            field=models.IntegerField(default=0),
        ),
    ]