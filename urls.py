# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from aldryn_django.utils import i18n_patterns
import aldryn_addons.urls
from django.views.generic import TemplateView

from stories.views import StoryCreateView

urlpatterns = [
    # add your own patterns here
    url(r'^$', TemplateView.as_view(template_name='base.html'), name='home'),
    url(r'^story/new$', StoryCreateView.as_view(), name='new_story'),
    ] + aldryn_addons.urls.patterns() + i18n_patterns(
    # add your own i18n patterns here
    *aldryn_addons.urls.i18n_patterns()  # MUST be the last entry!
)
