# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 06:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reg_sub', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='qboxuser',
            options={'verbose_name': 'Qboxuser', 'verbose_name_plural': 'Qboxusers'},
        ),
    ]