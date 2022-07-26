from django.db import models
from django.utils.translation import gettext_lazy as _
from countries.models import Country

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

    def __str__(self):
        return self.title


class CountryLanguage(models.Model):
    '''CountryLanguage'''
    COUNTRY_LANGUAGE_STATUS = (
        (1, _('Active')),
        (2, _('Inactive')),
        (3, _('Deleted')),
    )
    title = models.CharField(max_length=256, null=False, blank=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country_language')
    language = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country_language_language')
    code = models.CharField(_('Country Code'), max_length=3, null=True, blank=True)
    status = models.IntegerField(choices=COUNTRY_LANGUAGE_STATUS, default=1)

    class Meta:
        verbose_name = _('Country Language')
        verbose_name_plural = _('Countries Language')
        db_table = 'countries_language'

    def __str__(self):
        return self.title
