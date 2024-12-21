from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse
from accounts.models import GuestEmail

User = settings.AUTH_USER_MODEL

class BillingProfile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True)
    email = models.EmailField()
    active = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    customer_id = models.CharField(max_length=120, null=True, blank=True)
