from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import FormView
from invitations.views import AcceptInvite, Invitation



#TODO: Cleanup, Pylint/Pylama
#TODO: Nice templates
#TODO: Invite_button, USER Dashboard or area
#TODO: Logout icon
from user_invitation.forms import InviteForm


def show_404(request):
    raise Http404()


class CustomerAcceptInvite(AcceptInvite):
    def post(self, *args, **kwargs):
        target = super(CustomerAcceptInvite, self).post(*args, **kwargs)
        accept_url = reverse_lazy('account_signup')
        if hasattr(target, 'url') and target.url == accept_url:
            invitation = self.get_object()
            target = redirect(target.url + invitation.key)
        return target

class CustomerSignUpView(FormView):
    template_name = 'registration/register.html'
    success_url = '/'
    form_class = UserCreationForm

    def form_valid(self, form):
        key = self.request.resolver_match.kwargs['key']
        invitation = get_object_or_404(Invitation, key=key)
        User = get_user_model()
        user = User.objects.create_user(form.cleaned_data['username'],
                                        invitation.email,
                                        form.cleaned_data['password1'])

        user.save()
        login(self.request, user)
        return super(CustomerSignUpView, self).form_valid(form)

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

