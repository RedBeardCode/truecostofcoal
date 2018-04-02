#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Testing the story creation
"""
from django.test import  mock

from stories.forms import StoryForm
from stories.models import Story
from stories.tests.language_request import LanguageRequestFactory
from stories.views import StoryCreateView




class TestStoryCreation(object):

    def test_render_view(self, admin_user):
        request = LanguageRequestFactory('en', admin_user).get('/story/new')
        response = StoryCreateView.as_view()(request)
        assert response.status_code == 200
        assert 'stories/story_form.html' in response.template_name
        response.render()
        assert b'id="id_title"' in response.content
        assert b'id="id_story"' in response.content
        assert b'id="id_region"' in response.content
        assert b'id="id_min_zoom"' in response.content


    @mock.patch('stories.models.Story.save', mock.MagicMock(name='save'))
    def test_submit_data(self, admin_user):
        request = LanguageRequestFactory('en', admin_user).post(
            '/story/view',
            {
                'title': 'test_title',
                'story': 'a short test story',
                'region': 'POLYGON (('
                          '556024.176254229 5942016.744659892,'
                          '560304.6498381989 5940144.037466906,'
                          '564432.2493655984 5944997.788763015,'
                          '557361.8242492196 5944997.788763015,'
                          '556024.176254229 5942016.744659892'
                          '))',
                'min_zoom': 5,
            },
        )
        response = StoryCreateView.as_view()(request)
        assert response.status_code == 302
        assert response.url == '/'
        assert Story.save.call_count == 1


    @mock.patch('stories.models.Story.save', mock.MagicMock(name='save'))
    @mock.patch('stories.forms.StoryForm.set_translation',
                mock.MagicMock(name='set_translation'))
    def test_from_language(self, admin_user):
        for i, lang in enumerate(['en', 'de', 'es']):
            request = LanguageRequestFactory(lang, admin_user).post(
                '/story/view',
                {
                    'title': 'test_title',
                    'story': 'a short test story',
                    'region': 'POLYGON (('
                              '556024.176254229 5942016.744659892,'
                              '560304.6498381989 5940144.037466906,'
                              '564432.2493655984 5944997.788763015,'
                              '557361.8242492196 5944997.788763015,'
                              '556024.176254229 5942016.744659892'
                              '))',
                    'min_zoom': 5,
                },
            )
            response = StoryCreateView.as_view()(request)
            assert response.status_code == 302
            assert StoryForm.set_translation.called_once_with(lang)
            assert Story.save.call_count == i+1



