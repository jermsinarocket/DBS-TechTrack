from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from datetime import datetime


class Session(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.TextField(default="123",blank=True)
    token_time = models.TimeField(blank=True)

    class Meta:
        app_label = "TechTrack"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Session.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
