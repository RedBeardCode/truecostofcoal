# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 21:53
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_auto_20170417_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='region',
            field=django.contrib.gis.db.models.fields.PolygonField(srid=4326),
        ),
    ]
