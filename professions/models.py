from django.db import models
from django.utils.translation import gettext_lazy as _


class Profession(models.Model):
    '''Profession'''
    PROFESSION_STATUS = (
        (1, _('Active')),
        (2, _('Inactive')),
        (3, _('Deleted')),
    )
    title = models.CharField(_('Profession'), max_length=255, blank=False, null=False, unique=True)
    # slug = models.SlugField(_('slug'), unique=True, blank=False, null=False)
    status = models.IntegerField(_('Status'), choices=PROFESSION_STATUS, default=1)

    class Meta:
        verbose_name = _('Profession')
        verbose_name_plural = _('Professions')
        db_table = 'professions'

    def __str__(self):
        return self.title
