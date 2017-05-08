# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.core.urlresolvers import reverse
from django.views.generic import CreateView

from stories.forms import StroyForm



class StoryCreateView(CreateView):
    template_name = 'stories/story_form.html'
    form_class = StroyForm
    #success_url = '/'

    def form_invalid(self, form):
        return super(StoryCreateView, self).form_invalid(form)
    
    def form_valid(self, form):
        return super(StoryCreateView, self).form_valid(form)

