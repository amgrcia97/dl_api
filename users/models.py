from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


class Country(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    code = models.CharField(_('Código Alpha3'), max_length=50, null=True, blank=True)
    alpha_2_code = models.CharField(_('Código Alpha2'), max_length=2, null=True, blank=False, default=None)


class User(AbstractBaseUser, PermissionsMixin):
    USER_STATUS = (
        (1, _('Active')),
        (2, _('Inactive')),
        (3, _('Deleted')),
        (4, _('Pre-registered')),
        (8, _('Locked'))
    )
    full_name = models.CharField(_('Full Name'), max_length=255)
    nick_name = models.CharField(_('Nickname'), max_length=255, null=True, blank=True, default=None)
    email = models.EmailField(_('Email Address'), blank=False, unique=True)
    birth_country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='birth_country')
    actual_country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='actual_country')
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=False)
    date_updated = models.DateTimeField(_('date changed'), auto_now=False)
    is_staff = models.BooleanField(_('is_staff'), default=False)
    is_superuser = models.BooleanField(_('is_superuser'), default=False)
    status = models.IntegerField(_('Status'), choices=USER_STATUS, default=4)

    class Meta:
        verbose_name = 'User'
        verbose_name_users = 'Users'

    def __str__(self):
        return self.full_name
