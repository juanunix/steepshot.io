# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-26 12:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_teammembers'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammembers',
            name='link_linkedin',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='teammembers',
            name='link_github',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]