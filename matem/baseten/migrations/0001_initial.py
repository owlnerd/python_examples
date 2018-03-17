# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-19 09:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mathematician',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=40)),
                ('lname', models.CharField(blank=True, max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Theorem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=100)),
                ('author', models.ManyToManyField(to='baseten.Mathematician')),
            ],
        ),
    ]
