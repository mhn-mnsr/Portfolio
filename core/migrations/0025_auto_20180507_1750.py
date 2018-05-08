# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20180126_1106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactdetails',
            name='mobile',
        ),
        migrations.AlterField(
            model_name='contactdetails',
            name='website',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='github_url',
            field=models.CharField(max_length=1000, blank=True),
        ),
    ]
