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
    # Use MyUserManager whenever migrations
    use_in_migrations = True

    # Check email and password
    def _create_user(self,email,password,**extra_fields):
        # If no email, raise error
        if not email:
            raise ValueError('users must have an email address')

        # If there is email and password 
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # Create user if email and passord (def _create_user) are ok, and password=None
    def create_user(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email,password,**extra_fields)

    # Create superuser    
    def create_superuser(self,email,password,**extra_fields):
        # If superuser, its ok
        extra_fields.setdefault('is_superuser',True)
        # If not superuser, raise error
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self._create_user(email,password,**extra_fields)


# MyUser model
class MyUser(AbstractBaseUser,PermissionsMixin):

    """My own custom user class"""

    email       = models.EmailField(_('email address'), max_length=255, unique=True)
    first_name  = models.CharField(_('first name'), max_length=50, blank=True)
    last_name   = models.CharField(_('last name'), max_length=50, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active   = models.BooleanField(_('Active'), default=True)
    is_admin    = models.BooleanField(_('Staff status'), default=False)
    is_employee = models.BooleanField(_('Employee status'), default=False)
    is_employer = models.BooleanField(_('Employer status'), default=False)    

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin