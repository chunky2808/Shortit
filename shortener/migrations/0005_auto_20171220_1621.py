# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-20 10:51
from __future__ import unicode_literals

from django.db import migrations, models
import shortener.validators


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0004_auto_20171127_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortiturl',
            name='url',
            field=models.CharField(max_length=200, validators=[shortener.validators.validate_url, shortener.validators.validate_dot_com]),
        ),
    ]