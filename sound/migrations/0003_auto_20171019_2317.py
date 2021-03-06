# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-19 23:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sound', '0002_show_show_num'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_type', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='show',
            name='file_type',
        ),
        migrations.AddField(
            model_name='pod',
            name='show',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sound.Show'),
        ),
    ]
