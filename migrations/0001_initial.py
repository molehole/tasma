# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 09:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Etykieta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nr', models.IntegerField()),
                ('ta', models.IntegerField()),
                ('data', models.DateField()),
                ('pozycja', models.IntegerField()),
                ('grupa', models.CharField(max_length=50)),
                ('element', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Etykieta',
                'verbose_name_plural': 'Etykiety',
            },
        ),
    ]
