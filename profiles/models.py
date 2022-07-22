from django.db import models
from django.utils.translation import gettext_lazy as _

PROFILE_STATUS = (
        (1, _('Active')),
        (2, _('Inactive')),
        (3, _('Deleted')),
    )


class Profile(models.Model):
    '''Profile'''
    title = models.CharField(_('Profile'), max_length=255, blank=False, null=False)
    slug = models.SlugField(_('slug'), unique=True, blank=False, null=False)
    status = models.IntegerField(_('Status'), choices=PROFILE_STATUS, default=1)

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')
        db_table = 'profiles'
