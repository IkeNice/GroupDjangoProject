# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-03-13 12:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20200313_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.TextField(verbose_name='Имя')),
                ('second_name', models.TextField(verbose_name='Фамилия')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='post_likes',
            field=models.IntegerField(default=0, verbose_name='Понравилось'),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 13, 15, 26, 37, 44822), verbose_name='Дата добавления'),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 13, 15, 26, 37, 44822), verbose_name='Дата обновления'),
        ),
    ]