# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.core.urlresolvers import reverse
from django.views.generic import CreateView

from stories.forms import StoryForm



class StoryCreateView(CreateView):
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