# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=64)),
                ('lname', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=128)),
                ('dob', models.DateField(auto_now=True)),
            ],
        ),
    ]
