# -*- coding: utf-8 -*-
from django.conf.urls import url
from aldryn_django.utils import i18n_patterns
import aldryn_addons.urls
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout
from stories.views import StoryCreateView, StoryView
from stories.views import login


urlpatterns = [
    # add your own patterns here
    url(r'^$', StoryView.as_view(), name='home'),
    url(r'^story/new$', login_required(StoryCreateView.as_view()), name='new_story'),
    url(r'login/$', login, name='tcoc_login'),
    url(r'logout/$' logout, {'next_page':'/'}, name='tcoc_logout'),
    ] + aldryn_addons.urls.patterns() + i18n_patterns(
    # add your own i18n patterns here
    *aldryn_addons.urls.i18n_patterns()  # MUST be the last entry!
)
