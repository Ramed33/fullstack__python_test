from django.db import models
from datetime import timedelta
from django.conf import settings
from django.urls import reverse
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager
)

from django.core.mail import send_mail
from django.template.loader import get_template
from django.utils import timezone

DEFAULT_ACTIVATION_DAYS = getattr(settings, 'DEFAULT_ACTIVATIONS_DAYS', 7)

class UserManager(BaseUserManager):
    def create_user(self, email, full_name=None, password=None, is_active=True, is_staff=False,
                    is_admin=False):
        if not email:
            raise ValueError("Los usuarios deben tener un correo")
        if not password:
            raise ValueError("Los usuarios deben tener una contraseña")
        user_obj = self.model(
            email = self.normalize_email(email),
            full_name = full_name
        )        
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.is_active = is_active
        user_obj.save(using=self._db)
        return user_obj
    
    def create_staffuser(self, email, full_name=None, password=None):
        user = self.create_user(
            email,
            full_name = full_name,
            password=password,
            is_staff=True
        )
        return user
    
    def create_superuser(self, email, full_name=None, password=None):
        user = self.create_user(
            email,
            full_name = full_name,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user
    
class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
        
    def get_full_name(self):
        if self.full_name:
            return self.full_name
        return self.email
        
    def get_short_name(self):
        return self.email
        
    def has_perm(self, perm, obj=None):
        return True
        
    def has_module_perms(self, app_label):
        return True
        
    @property
    def is_staff(self):
        if self.is_admin:
            return True
        return self.staff
        
    @property
    def is_admin(self):
        return self.admin
    
class GuestEmail(models.Model):
    email = models.EmailField()
    active = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email