# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-09 17:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='brief',
            field=models.CharField(max_length=5000),
        ),
    ]
