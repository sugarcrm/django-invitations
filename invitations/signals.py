from django.dispatch import Signal

invite_url_sent = Signal()
"""
@receiver(invite_url_sent, sender=Invitation)
def invite_url_sent(sender, instance, invite_url_sent, inviter, **kwargs):
    pass
"""

invite_accepted = Signal()
"""
@receiver(invite_accepted, sender=auth.models.AnonymousUser)
def invite_accepted(sender, request, email, **kwargs):
    pass
"""
