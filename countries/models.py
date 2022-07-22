from django.db import models
from django.utils.translation import gettext_lazy as _


class Country(models.Model):
    '''Country'''
    COUNTRY_STATUS = (
        (1, _('Active')),
        (2, _('Inactive')),
        (3, _('Deleted')),
    )
    name = models.CharField(_('Country'), max_length=256, null=False, blank=False)
    code = models.CharField(_('Country Code'), max_length=3, null=True, blank=True)
    status = models.IntegerField(choices=COUNTRY_STATUS, default=1)

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')
        db_table = 'countries'


class CountryLanguage(models.Model):
    '''CountryLanguage'''
    COUNTRY_LANGUAGE_STATUS = (
        (1, _('Active')),
        (2, _('Inactive')),
        (3, _('Deleted')),
    )
    title = models.CharField(max_length=256, null=False, blank=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country_language')
    code = models.CharField(_('Country Code'), max_length=3, null=True, blank=True)
    status = models.IntegerField(choices=COUNTRY_LANGUAGE_STATUS, default=1)

    class Meta:
        verbose_name = _('Country Language')
        verbose_name_plural = _('Countries Language')
        db_table = 'countries_language'
