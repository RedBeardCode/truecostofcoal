import re

# Create your tests here.
from invitations.views import SendInvite

from random import randint

from django.core import mail
from invitations.models import Invitation



class TestUserInvitationBackEnd:

    def test_send_invitation(self, db, rf, mailoutbox):
        invite = Invitation.create('{0}@example.com'.format(
            randint(11111111, 99999999)))
        mails_before = len(mailoutbox)
        invite.send_invitation(rf.get(''))
        assert len(mailoutbox) == mails_before+1
        assert invite.key in mailoutbox[-1].body
        invite.delete()


class TestInvitationFrontEnd:

    def test_register_no_invitation(self, client, db):
        response = client.get('/accept-invite/register/')
        assert response.status_code == 404

    def test_send_invitation(self, rf, db, admin_user, client):
        invite_request = rf.post('')
        invite_request.user = admin_user
        invite_request.POST ={'email': '{0}@example.com'.format(
            randint(11111111, 99999999))}
        mails_before = len(mail.outbox)
        response = SendInvite.as_view()(invite_request)
        assert len(mail.outbox) == mails_before+1
        invite_mail = mail.outbox[-1]
        key = re.search(
            '.*http://.*/invitations/accept-invite/(.*)\s',
            invite_mail.body).groups()[0]
        response = client.get('/invitations/accept-invite/{key}'.format(key=key))

        assert response.status_code == 302
        assert response.url  == '/accept-invite/register/{key}'.format(key=key)


