# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 19:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0002_auto_20170703_2123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chair',
            old_name='created_at',
            new_name='date',
        ),
    ]
