# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 19:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mfc', '0002_auto_20170208_1014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название документа')),
            ],
        ),
        migrations.CreateModel(
            name='List_of_requests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.PositiveIntegerField(unique=True, verbose_name='Серийный номер')),
                ('surname', models.CharField(max_length=40, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('middle_name', models.CharField(max_length=35, verbose_name='Отчество')),
                ('date_of_birth', models.DateField(verbose_name='Дата рождения')),
                ('place_of_birth', models.CharField(max_length=100, verbose_name='Место рождения')),
                ('issued_by', models.CharField(max_length=100, verbose_name='Кем выдан')),
                ('date_of_issue', models.DateField(verbose_name='Дата выдачи')),
                ('place_of_registration', models.CharField(max_length=100, verbose_name='Место прописки')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_beginning', models.DateTimeField()),
                ('date_of_ending', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Наименование услуги')),
                ('description', models.TextField(verbose_name='Описание')),
                ('cost', models.CharField(max_length=150, verbose_name='Стоимость')),
                ('documents', models.TextField(verbose_name='Перечень необходимых документов')),
                ('count_of_documents', models.IntegerField(default=0, verbose_name='Кол-во необходимых документов')),
            ],
        ),
        migrations.CreateModel(
            name='Snils',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=14, unique=True, verbose_name='Серийный номер')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=20)),
                ('snils', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mfc.Snils')),
            ],
        ),
        migrations.RenameField(
            model_name='image',
            old_name='picture',
            new_name='photo',
        ),
        migrations.AlterField(
            model_name='new',
            name='picture',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='mfc.Image', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='new',
            name='time_of_editing',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата изменения'),
        ),
        migrations.AlterField(
            model_name='new',
            name='time_of_publishing',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления'),
        ),
        migrations.AddField(
            model_name='request',
            name='login',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='mfc.User'),
        ),
        migrations.AddField(
            model_name='request',
            name='participant_one',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='participant_one', to='mfc.Document'),
        ),
        migrations.AddField(
            model_name='request',
            name='participant_three',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='participant_three', to='mfc.Document'),
        ),
        migrations.AddField(
            model_name='request',
            name='participant_two',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='participant_two', to='mfc.Document'),
        ),
        migrations.AddField(
            model_name='request',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mfc.Service'),
        ),
        migrations.AddField(
            model_name='passport',
            name='login',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='mfc.User'),
        ),
        migrations.AddField(
            model_name='list_of_requests',
            name='request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mfc.Request'),
        ),
        migrations.AddField(
            model_name='document',
            name='login',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='mfc.User'),
        ),
        migrations.AddField(
            model_name='document',
            name='picture',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='mfc.Image', verbose_name='Изображение'),
        ),
    ]