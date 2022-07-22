from django.db import models
from django.utils.translation import gettext_lazy as _

LANGUAGE_STATUS = (
        (1, _('Active')),
        (2, _('Inactive')),
        (3, _('Deleted')),
    )


class Language(models.Model):
    '''Language'''
    title = models.CharField(_('Language'), max_length=255, blank=False, null=False)
    code = models.SlugField(_('code'), unique=True, blank=False, null=False)
    status = models.IntegerField(_('Status'), choices=LANGUAGE_STATUS, default=1)

    class Meta:
        verbose_name = _('Language')
        verbose_name_plural = _('Languages')
        db_table = 'languages'
