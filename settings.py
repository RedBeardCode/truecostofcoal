# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _

INSTALLED_ADDONS = [
    # <INSTALLED_ADDONS>  # Warning: text inside the INSTALLED_ADDONS tags is auto-generated. Manual changes will be overwritten.
    'aldryn-addons',
    'aldryn-django',
    'aldryn-sso',
    'aldryn-devsync',
    'aldryn-django-debug-toolbar',
    # </INSTALLED_ADDONS>
]

import aldryn_addons.settings
aldryn_addons.settings.load(locals())



# all django settings can be altered here

INSTALLED_APPS.extend([
    # add your project specific apps here
    'nece',
    'crispy_forms',
    'invitations',
    'user_invitation',
    'stories',
])

MIDDLEWARE_CLASSES.extend([
    # add your own middlewares here
    'django.middleware.locale.LocaleMiddleware',
])


CRISPY_TEMPLATE_PACK = 'bootstrap3'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS' :['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'aldryn_snake.template_api.template_processor',
            ],
        },
    },
]

LANGUAGES =  [
    ('de', _('German')),
    ('en', _('English')),
]

LOGIN_URL = 'tcoc_login'
LOGOUT_URL = 'tcoc_logout'
LOGIN_REDIRECT_URL = '/'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ACCEPT_INVITE_AFTER_SIGNUP=True