# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-01 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mfc', '0019_auto_20170501_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='snils_number',
            field=models.CharField(max_length=11, unique=True, verbose_name='Номер СНИЛС'),
        ),
    ]