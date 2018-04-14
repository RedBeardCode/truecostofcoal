# -*- coding: utf-8 -*-
from functools import partial

from aldryn_client import forms


class Form(forms.BaseForm):

    enable_debug_toolbar = forms.CheckboxField(
        'Enable Django Debug Toolbar',
        required=False,
        initial=True,
    )

    # The generally recommended position for the DebugToolbarMiddleware is immediately after the
    # GZipMiddleware. See https://django-debug-toolbar.readthedocs.io/en/stable/installation.html#middleware
    # and https://django-debug-toolbar.readthedocs.io/en/stable/tips.html#middleware-isn-t-working-correctly

    POSITIONS = [
        ["top", "As close to the top as possible"],
        ["end", "As close to the end as possible"],

    ]

    toolbar_middleware_position = forms.SelectField(
        'DebugToolbarMiddleware position',
        help_text="Position in the middleware list",
        choices=POSITIONS,
        initial="top",
    )


    def _show_toolbar(self, request):
        return True

    def to_settings(self, data, settings):

        if settings["DEBUG"] and data['enable_debug_toolbar']:

            settings["INSTALLED_APPS"].extend(["debug_toolbar"])

            settings["DEBUG_TOOLBAR_CONFIG"] = {"SHOW_TOOLBAR_CALLBACK": self._show_toolbar}

            middleware = settings["MIDDLEWARE_CLASSES"]
            debug_toolbar_middleware = "debug_toolbar.middleware.DebugToolbarMiddleware"
            debug_toolbar_middleware_position = data["toolbar_middleware_position"]

            if "django.middleware.gzip.GZipMiddleware" in middleware and debug_toolbar_middleware_position == "top":

                middleware.insert(
                    middleware.index("django.middleware.gzip.GZipMiddleware") + 1,
                    debug_toolbar_middleware
                )

            elif debug_toolbar_middleware_position == "end":
                middleware.append(debug_toolbar_middleware)

            else:
                middleware.insert(0, debug_toolbar_middleware)

            settings['ADDON_URLS'].append('aldryn_django_debug_toolbar.urls')

        return settings
