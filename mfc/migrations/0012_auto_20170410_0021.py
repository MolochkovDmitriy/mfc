# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-09 21:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mfc', '0011_auto_20170409_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='service_fk',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='mfc.Service'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='request',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Наименование заявки'),
        ),
    ]