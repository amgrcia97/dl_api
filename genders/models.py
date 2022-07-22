from django.db import models
from django.utils.translation import gettext_lazy as _


class Gender(models.Model):
    '''Gender'''
    GENDER_STATUS = (
        (1, _('Active')),
        (2, _('Inactive')),
        (3, _('Deleted')),
    )
    title = models.CharField(_('Gender'), max_length=255, blank=False, null=False)
    slug = models.SlugField(_('Slug'), unique=True)
    status = models.IntegerField(_('Status'), choices=GENDER_STATUS, default=2)

    class Meta:
        verbose_name = _('Gender')
        verbose_name_plural = _('Genders')
        db_table = 'genders'
