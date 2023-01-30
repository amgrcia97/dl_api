from django.db import models
from django.utils.translation import gettext_lazy as _
from addresses.models import Country


class Language(models.Model):
    '''Language'''
    title = models.CharField(_('Language'), max_length=255, blank=False, null=False)
    code = models.SlugField(_('Code'), unique=True, blank=False, null=False)
    status = models.BooleanField(_('Active?'), default=True)

    class Meta:
        verbose_name = _('Language')
        verbose_name_plural = _('Languages')
        db_table = 'languages'

    def __str__(self):
        return self.title


class CountryLanguage(models.Model):
    '''CountryLanguage'''
    code = models.CharField(_('Country Language Code'), max_length=3, null=True, blank=True, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country_language')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='country_language_language')
    status = models.BooleanField(_('Active?'), default=True)

    class Meta:
        verbose_name = _('Country Language')
        verbose_name_plural = _('Countries Language')
        db_table = 'countries_language'

    def __str__(self):
        return self.code
