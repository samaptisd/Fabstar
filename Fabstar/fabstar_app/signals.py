from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # Only save the profile if it exists
    if hasattr(instance, 'profile'):
        instance.profile.save()


import logging
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver

# Get the custom logger
user_logger = logging.getLogger('user_activity')

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    ip = request.META.get('REMOTE_ADDR', 'Unknown IP')
    user_agent = request.META.get('HTTP_USER_AGENT', 'Unknown Browser')
    user_logger.info(f"[LOGIN] User: {user.username}, IP: {ip}, Browser: {user_agent}")

@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    ip = request.META.get('REMOTE_ADDR', 'Unknown IP')
    user_logger.info(f"[LOGOUT] User: {user.username}, IP: {ip}")
