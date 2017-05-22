# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib.gis.admin.options import spherical_mercator_srid

from stories.models import Story

class StoryGeoAdmin(OSMGeoAdmin):
    map_template = 'story_admin.html'

    num_zoom = 7
    map_srid = 3857

    default_lon = -14406669
    default_lat = 16718459
    default_zoom = 3
    point_zoom =  7
    #units = 'm'
    debug = False

admin.site.register(Story, StoryGeoAdmin)