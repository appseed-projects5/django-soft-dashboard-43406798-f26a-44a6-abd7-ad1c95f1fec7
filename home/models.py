# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Usercred(models.Model):

    #__Usercred_FIELDS__
    uname = models.CharField(max_length=255, null=True, blank=True)

    #__Usercred_FIELDS__END

    class Meta:
        verbose_name        = _("Usercred")
        verbose_name_plural = _("Usercred")


class Userscore(models.Model):

    #__Userscore_FIELDS__

    #__Userscore_FIELDS__END

    class Meta:
        verbose_name        = _("Userscore")
        verbose_name_plural = _("Userscore")



#__MODELS__END
