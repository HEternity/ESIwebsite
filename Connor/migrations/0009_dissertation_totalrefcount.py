# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-29 01:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Connor', '0008_auto_20170613_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='dissertation',
            name='TOTALREFCOUNT',
            field=models.IntegerField(null=True),
        ),
    ]
