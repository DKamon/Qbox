from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import is_password_usable
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
import datetime


@python_2_unicode_compatible    #for python 2 compatibility
class Subscribe(models.Model):
    name = models.CharField(max_length=40, blank=False, default="")
    email = models.EmailField(blank=False)
    subject = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return u'%s' % (self.email)


@python_2_unicode_compatible    #for python 2 compatibility
class Intern(models.Model):
    name = models.CharField(max_length=40, blank=False)
    email = models.EmailField(blank=False)
    contactno = models.CharField(max_length=15, blank=True, default="")
    interests = models.TextField(max_length=100, blank=False)
    def __str__(self):
        return u'%s' % (self.email)
