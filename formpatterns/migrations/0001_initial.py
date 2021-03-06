# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-02 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormFields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fieldName', models.CharField(max_length=50)),
                ('field_types', models.CharField(choices=[('txt', 'txt'), ('email', 'email'), ('phone', 'phone')], default='txt', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='FormPattern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formName', models.CharField(max_length=50)),
                ('fields', models.ManyToManyField(to='formpatterns.FormFields')),
            ],
        ),
    ]
