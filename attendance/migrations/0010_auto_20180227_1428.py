# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-27 08:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0009_auto_20180227_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='date_time',
            field=models.DateField(),
        ),
    ]