# -*- coding: utf-8 -*-
from django.conf.urls import url
from aldryn_django.utils import i18n_patterns
import aldryn_addons.urls
from django.contrib.auth.views import LogoutView, LoginView
from stories.views import StoryCreateView, StoryView


urlpatterns = [
    # add your own patterns here
    url(r'^$', StoryView.as_view(), name='home'),
    url(r'^story/new$', StoryCreateView.as_view(), name='new_story'),
    url(r'login/$', LoginView.as_view(), name='tcoc_login'),
    url(r'logout/$', LogoutView.as_view(next_page='/'), name='tcoc_logout'),
    ] + aldryn_addons.urls.patterns() + i18n_patterns(
    # add your own i18n patterns here
    *aldryn_addons.urls.i18n_patterns()  # MUST be the last entry!
)
