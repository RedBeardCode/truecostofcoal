# -*- coding: utf-8 -*-
import dj_email_url
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
    'django_extensions',
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

email_config = dj_email_url.config()
if 'EMAIL_BACKEND' in email_config:
    EMAIL_BACKEND = email_config['EMAIL_BACKEND']
    EMAIL_HOST_USER = email_config['EMAIL_HOST_USER']
    EMAIL_HOST_PASSWORD = email_config['EMAIL_HOST_PASSWORD']
    EMAIL_HOST = email_config['EMAIL_HOST']
    EMAIL_PORT = email_config['EMAIL_PORT']
    EMAIL_USE_TLS = email_config['EMAIL_USE_TLS']
    EMAIL_USE_SSL = email_config['EMAIL_USE_SSL']

ACCEPT_INVITE_AFTER_SIGNUP=True