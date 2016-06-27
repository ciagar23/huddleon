# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-27 05:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=200)),
                ('reciever', models.CharField(max_length=200)),
                ('message', models.TextField(null=True)),
                ('create_datetime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]