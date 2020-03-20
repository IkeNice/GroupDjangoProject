# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-03-13 13:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20200313_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='genre',
            field=models.CharField(choices=[('r1', 'Роман'), ('p', 'Поэма'), ('r2', 'Рассказ')], default='r1', max_length=50, verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 13, 16, 13, 24, 349806), verbose_name='Дата добавления'),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 13, 16, 13, 24, 349806), verbose_name='Дата обновления'),
        ),
    ]
