#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

"""
from django.contrib.gis.forms import PolygonField, OSMWidget, Textarea
from django.forms import ModelForm, CharField, IntegerField

from stories.models import Story



class StroyForm(ModelForm):
    class Meta:
        fields = ['title', 'story', 'region', 'min_zoom']
        model = Story


    title = CharField()
    story = CharField(widget=Textarea())
    min_zoom = IntegerField()
    region = PolygonField(widget=OSMWidget(attrs={'display_raw': True}))
    
    def save(self, commit=True):
        return super(StroyForm, self).save(commit=commit)

