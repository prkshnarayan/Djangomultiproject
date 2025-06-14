# salesapp/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student
from .utils.email_utils import send_welcome_email


@receiver(post_save, sender=Student)
def send_welcome_email_on_creation(sender, instance, created, **kwargs):
    if created:
        send_welcome_email(instance)
