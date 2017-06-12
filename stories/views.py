# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.contrib.auth import get_user_model, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.serializers import serialize
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, FormView
from braces.views import AjaxResponseMixin
from invitations.views import Invitation, AcceptInvite

from stories.forms import StoryForm
from stories.models import Story

class StoryCreateView(LoginRequiredMixin, CreateView):
    template_name = 'stories/story_form.html'
    form_class = StoryForm

    def form_invalid(self, form):
        return super(StoryCreateView, self).form_invalid(form)
    
    def form_valid(self, form):
        return super(StoryCreateView, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(StoryCreateView, self).get_form_kwargs()
        kwargs['language'] = self.request.LANGUAGE_CODE
        return kwargs


class StoryView(AjaxResponseMixin, TemplateView):
    template_name = "base.html"
    def post_ajax(self, request, *args, **kwargs):
        geojson = serialize(
            'geojson',
            Story.objects.filter(min_zoom__lte=request.POST['zoomlevel']),
            geometry_field='region',
            fields=('title', 'story')
        )
        return HttpResponse(geojson, content_type='application/json')


