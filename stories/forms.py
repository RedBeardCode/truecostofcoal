#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

"""
from django.contrib.gis.forms import PolygonField, OSMWidget, Textarea
from django.forms import ModelForm, CharField, IntegerField, EmailField, Form, TextInput
from django.template.loader import get_template

from stories.models import Story



class TCOCWidget(OSMWidget):
    def render(self, name, value, attrs=None, renderer=None):
        html = get_template('TCOCWidget.html')
        return html.render()


class StoryForm(ModelForm):
    class Meta:
        fields = ['title', 'story', 'region', 'min_zoom']
        model = Story


    title = CharField()
    story = CharField(widget=Textarea())
    min_zoom = IntegerField()
    region = PolygonField(widget=TCOCWidget())
    
    def __init__(self, *arg, **kwargs):
        self.__language = kwargs.pop('language', 'en')
        super(StoryForm, self).__init__(*arg, **kwargs)

    def set_translation(self, language):
        self.instance.translate(
            language,
            title=self.cleaned_data['title'],
            story=self.cleaned_data['story']
        )

    def save(self, commit=True):
        ret_val = super(StoryForm, self).save(commit)
        self.set_translation(self.__language)
        return ret_val