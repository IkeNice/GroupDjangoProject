# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-03-13 14:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_auto_20200313_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 13, 17, 49, 42, 524731), verbose_name='Дата добавления'),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 13, 17, 49, 42, 524731), verbose_name='Дата обновления'),
        ),
    ]
