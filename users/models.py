from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


STATUS_CHOICES = (
    (1, _('Active')),
    (2, _('Inactive')),
    (3, _('Deleted')),
)


class Country(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    code = models.CharField(_('Código Alpha3'), max_length=50, null=True, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    class Meta:
        verbose_name = _('Country')
        verbose_name_users = _('Countries')

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    initials = models.CharField(max_length=10, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country_states')
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    class Meta:
        verbose_name = _('City')
        verbose_name_users = _('Cites')

    def __str__(self):
        return self.name


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
    actual_city = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='actual_country')
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=False)
    date_updated = models.DateTimeField(_('date changed'), auto_now=False)
    is_staff = models.BooleanField(_('is_staff'), default=False)
    is_superuser = models.BooleanField(_('is_superuser'), default=False)
    status = models.IntegerField(_('Status'), choices=USER_STATUS, default=4)

    class Meta:
        verbose_name = _('User')
        verbose_name_users = _('Users')

    def __str__(self):
        return self.full_name
