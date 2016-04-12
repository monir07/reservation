# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 03:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_auto_20160412_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train',
            name='second_ac',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='train',
            name='sleeper',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='train',
            name='third_ac',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.DeleteModel(
            name='Seat',
        ),
    ]
