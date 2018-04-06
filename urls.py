# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from aldryn_django.utils import i18n_patterns
import aldryn_addons.urls
from django.contrib.auth.views import LogoutView, LoginView


from stories.views import StoryCreateView, StoryView
from user_invitation.views import CustomerAcceptInvite, CustomerSignUpView, SendInvite
from user_invitation.views import show_404

urlpatterns = [
    # add your own patterns here
    url(r'^invitations/send-invite/$', SendInvite.as_view(), name='send-invite'),
    url(r'^invitations/accept-invite/(?P<key>\w+)/?$',
        CustomerAcceptInvite.as_view(), name='accept-invite'),
    url(r'^invitations/', include('invitations.urls',
                                  namespace='invitations')),

    url(r'^$', StoryView.as_view(), name='home'),
    url('^accept-invite/register/$', show_404,
        name='account_signup'),
    url('^accept-invite/register/(?P<key>\w+)/?$',
        CustomerSignUpView.as_view(), name='account_signup'),
    url(r'^story/new$', StoryCreateView.as_view(), name='new_story'),
    url(r'login/$', LoginView.as_view(), name='tcoc_login'),
    url(r'logout/$', LogoutView.as_view(next_page='/'), name='tcoc_logout'),
    ] + aldryn_addons.urls.patterns() + i18n_patterns(
    # add your own i18n patterns here
    *aldryn_addons.urls.i18n_patterns()  # MUST be the last entry!
)
