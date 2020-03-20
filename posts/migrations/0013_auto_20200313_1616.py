# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-03-13 13:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_auto_20200313_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 13, 16, 16, 42, 97443), verbose_name='Дата добавления'),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 13, 16, 16, 42, 97443), verbose_name='Дата обновления'),
        ),
    ]