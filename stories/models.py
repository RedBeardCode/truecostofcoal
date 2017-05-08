# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db.models import PolygonField
from nece.models import TranslationModel

class Story(TranslationModel):
    story = models.TextField(verbose_name='The hole Story')
    title = models.CharField(verbose_name='Title', max_length=100)
    region = PolygonField(srid=4326, blank=True, null=True)
    min_zoom = models.IntegerField(verbose_name='Minimal zoom')

    class Meta:
        translatable_fields = ('title', 'story')

    def get_absolute_url(self):
        return '/'