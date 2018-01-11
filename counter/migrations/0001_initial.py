# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-01-09 13:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shortener', '0005_auto_20171220_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClickEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('shortit_Url', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shortener.shortitURL')),
            ],
        ),
    ]
