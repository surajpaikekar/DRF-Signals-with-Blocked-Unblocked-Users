from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import BlockedUser
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=BlockedUser)
def update_blocked_user_list(sender, instance, created, **kwargs):
    if created:
        logger.info(f"Blocked user: {instance.blocked_user.username} by {instance.user.username}")
    else:
        logger.info(f"Blocked user relationship updated: {instance.blocked_user.username} by {instance.user.username}")
