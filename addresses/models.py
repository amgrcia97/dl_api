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


class State(models.Model):
    '''State'''
    STATE_STATUS = (
        (1, _('Active')),
        (2, _('Inactive')),
        (3, _('Deleted')),
    )
    name = models.CharField(_('State'), max_length=256, null=False, blank=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country_states')
    status = models.IntegerField(choices=STATE_STATUS, default=1)

    class Meta:
        verbose_name = _('State')
        verbose_name_plural = _('States')
        db_table = 'states'


class City(models.Model):
    '''City'''
    CITY_STATUS = (
        (1, _('Active')),
        (2, _('Inactive')),
        (3, _('Deleted')),
    )
    name = models.CharField(_('City'), max_length=256, null=False, blank=False)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='state_cities')
    status = models.IntegerField(choices=CITY_STATUS, default=1)

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Cities')
        db_table = 'cities'


class Address(models.Model):
    '''Address'''
    address = models.CharField(_('Address'), max_length=512, blank=False, null=False)
    number = models.CharField(_('Number'), max_length=128, blank=True, null=True)
    complement = models.CharField(_('Complement'), max_length=128, blank=True, null=True)
    neighborhood = models.CharField(_('Neighborhood'), max_length=128, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='address_city')

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')
        db_table = 'addresses'
