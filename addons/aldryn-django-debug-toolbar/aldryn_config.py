# -*- coding: utf-8 -*-
from functools import partial

from aldryn_client import forms


class Form(forms.BaseForm):
    enable_debug_toolbar = forms.CheckboxField(
        'Enable Django Debug Toolbar',
        required=False,
        initial=True,
    )

    def _show_toolbar(self, request):
        return True

    def to_settings(self, data, settings):
        enable_debug_toolbar = data['enable_debug_toolbar']

        from aldryn_addons.utils import djsenv
        env = partial(djsenv, settings=settings)
        env_stage = '' if env('STAGE') is None else str(env('STAGE'))
        development_mode = True if env_stage in ['test', 'local'] else False

        if enable_debug_toolbar and development_mode:
            settings['INSTALLED_APPS'].extend([
                'debug_toolbar',
            ])
            settings['ADDON_URLS'].append('aldryn_django_debug_toolbar.urls')
            settings['DEBUG_TOOLBAR_CONFIG'] = {
                'DEBUG_TOOLBAR_PATCH_SETTINGS': False,
                'SHOW_TOOLBAR_CALLBACK': self._show_toolbar,
                'DISABLE_GZIP': True,
            }
        return settings
