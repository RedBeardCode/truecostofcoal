from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.forms import Form, EmailField, TextInput
from invitations.adapters import get_invitations_adapter
from invitations.exceptions import AlreadyInvited, AlreadyAccepted, UserRegisteredEmail
from invitations.models import Invitation


class CleanEmailMixin(object):

    last_token = None

    def validate_invitation(self, email):
        if Invitation.objects.all_valid().filter(
                email__iexact=email, accepted=False):
            raise AlreadyInvited
        elif Invitation.objects.filter(
                email__iexact=email, accepted=True):
            raise AlreadyAccepted
        elif get_user_model().objects.filter(email__iexact=email):
            raise UserRegisteredEmail
        else:
            return True

    def clean_email(self):
        email = self.cleaned_data["email"]
        email = get_invitations_adapter().clean_email(email)
        if self.last_token != self.data['csrfmiddlewaretoken']:
            errors = {
                "already_invited": _("This e-mail address has already been"
                                     " invited."),
                "already_accepted": _("This e-mail address has already"
                                      " accepted an invite."),
                "email_in_use": _("An active user is using this e-mail address"),
            }
            try:
                CleanEmailMixin.last_token = self.data['csrfmiddlewaretoken']
                self.validate_invitation(email)
            except(AlreadyInvited):
                raise ValidationError(errors["already_invited"])
            except(AlreadyAccepted):
                raise ValidationError(errors["already_accepted"])
            except(UserRegisteredEmail):
                raise ValidationError(errors["email_in_use"])
        return email


class InviteForm(Form, CleanEmailMixin):

    email = EmailField(
        label=_("E-mail"),
        required=True,
        widget=TextInput(
            attrs={"type": "email", "size": "30"}), initial="")

    def save(self, email):
        return Invitation.create(email=email)
