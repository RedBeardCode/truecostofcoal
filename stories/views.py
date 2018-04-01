# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.serializers import serialize
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView, FormView
from django.utils.translation import ugettext_lazy as _
from braces.views import AjaxResponseMixin

from stories.forms import StoryForm, InviteForm
from stories.models import Story

class SendInvite(FormView):
    template_name = 'invitations/forms/_invite.html'
    form_class = InviteForm

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(SendInvite, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        email = form.cleaned_data["email"]

        try:
            invite = form.save(email)
            invite.inviter = self.request.user
            invite.save()
            invite.send_invitation(self.request)
        except Exception:
            return self.form_invalid(form)
        return self.render_to_response(
            self.get_context_data(
                success_message=_('%(email)s has been invited') % {
                    "email": email}))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class StoryCreateView(LoginRequiredMixin, CreateView):
    template_name = 'stories/story_form.html'
    form_class = StoryForm

    def form_invalid(self, form):
        return super(StoryCreateView, self).form_invalid(form)
    
    def form_valid(self, form):
        return super(StoryCreateView, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(StoryCreateView, self).get_form_kwargs()
        kwargs['language'] = self.request.LANGUAGE_CODE
        return kwargs


class StoryView(AjaxResponseMixin, TemplateView):
    template_name = "base.html"
    def post_ajax(self, request, *args, **kwargs):
        geojson = serialize(
            'geojson',
            Story.objects.filter(min_zoom__lte=request.POST['zoomlevel']),
            geometry_field='region',
            fields=('title', 'story')
        )
        return HttpResponse(geojson, content_type='application/json')


