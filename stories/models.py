# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db.models import PolygonField

class Story(models.Model):
    name = models.CharField(verbose_name='Title', max_length=100)
    region = PolygonField(srid=4326)