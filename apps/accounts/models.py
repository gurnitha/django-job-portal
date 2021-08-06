# apps/accounts/models.py

# Django modules
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import (
	        AbstractBaseUser, 
	        BaseUserManager, 
	        PermissionsMixin)
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# Locals

# Create your models here

# MyUserManager model
class MyUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError('users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email,password,**extra_fields)


    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_superuser',True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self._create_user(email,password,**extra_fields)

# MyUser model
class MyUser(AbstractBaseUser,PermissionsMixin):
    """My own custom user class"""

    email = models.EmailField(max_length=255, unique=True, db_index=True, verbose_name=_('email address'))
    first_name = models.CharField(max_length=50,blank=False)
    last_name = models.CharField(max_length=50,blank=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)    

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """Return the email."""
        return self.email

    def get_short_name(self):
        """Return the email."""
        return self.email
