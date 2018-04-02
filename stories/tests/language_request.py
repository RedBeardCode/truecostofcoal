#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Mock request with language field
"""
from django.test import RequestFactory


class LanguageRequestFactory(RequestFactory):

    def __init__(self, language, user, *args, **kwargs):
        self.__language = language
        self.user = user
        super(LanguageRequestFactory, self).__init__(*args, **kwargs)

    def request(self, **request):
        request = super(LanguageRequestFactory, self).request(**request)
        request.LANGUAGE_CODE = self.__language
        request.user = self.user
        return request

