# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib.gis.admin.options import spherical_mercator_srid

from stories.models import Story

class StoryGeoAdmin(OSMGeoAdmin):
    map_template = 'story_admin.html'

    num_zoom = 7
    # map_srid = 4326

    default_lon = -15000000
    default_lat = 17500000
    default_zoom = 3
    #max_extent = '-20000000, 18300000,  -8800000, 25000000 '
    #max_resolution = '1.0339'
    point_zoom =  7
    #units = 'm'

admin.site.register(Story, StoryGeoAdmin)