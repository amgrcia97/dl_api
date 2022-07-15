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
        verbose_name_plural = _('Countries')
        db_table = 'countries'

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    initials = models.CharField(max_length=10, null=False, blank=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country_states')
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    class Meta:
        verbose_name = _('State')
        verbose_name_plural = _('States')
        db_table = 'states'


class City(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    initials = models.CharField(max_length=10, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country_states')
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Cites')

    def __str__(self):
        return self.name


class Address(models.Model):
    address = models.CharField(_('Adress'), max_length=512, blank=False, null=False)
    number = models.CharField(_('Number'), max_length=128, blank=True, null=True)
    complement = models.CharField(_('Complement'), max_length=128, blank=True, null=True)
    neighborhood = models.CharField(_('Neighborhood'), max_length=128, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='address_city')
    postal_code = models.CharField(_('Postal Code'), max_length=128, blank=True, null=True)

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')
        db_table = 'addresses'


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
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=False)
    date_updated = models.DateTimeField(_('date changed'), auto_now=False)
    is_staff = models.BooleanField(_('is_staff'), default=False)
    is_superuser = models.BooleanField(_('is_superuser'), default=False)
    status = models.IntegerField(_('Status'), choices=USER_STATUS, default=4)

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        db_table = 'users'


class AgeGroup(models.Model):
    title = models.CharField(_('Título'), max_length=120, null=False, blank=False)
    slug = models.SlugField(_('Slug'), blank=False, null=False, unique=True)
    status = models.IntegerField(_('Status'), choices=STATUS_CHOICES, default=1)

    class Meta:
        verbose_name = _('AgeGroup')
        verbose_name_plural = _('AgeGroups')
        db_table = 'age_groups'


class Gender(models.Model):
    title = models.CharField(_('gender'), max_length=255, blank=False, null=False, unique=True)

    class Meta:
        verbose_name = _('Gender')
        verbose_name_plural = _('Genders')
        db_table = 'genders'


class Phone(models.Model):
    phone = models.CharField(_('Telefone'), max_length=50, blank=False, null=False, unique=True)

    class Meta:
        verbose_name = _('Phone')
        verbose_name_plural = _('Phones')
        db_table = 'phone'


class Profession(models.Model):
    profession = models.CharField(_('Profession'), max_length=100, blank=False, null=False, unique=True)

    class Meta:
        verbose_name = _('Profession')
        verbose_name_plural = _('Professions')
        db_table = 'professions'


USER_TYPE_CHOICES = (
    (1, _('Student')),
    (2, _('Teacher')),
    (3, _('Student and Teacher')),
)


class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='user_data')
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=False, related_name='user_gender')
    age_group = models.ForeignKey(AgeGroup, on_delete=models.CASCADE, null=True, related_name='user_age_group')
    birthday = models.DateField(_('Birth Date'), auto_now=False, null=True)
    document = models.CharField(_('Document'), max_length=255, blank=True, null=True, unique=True)
    addresses = models.ManyToManyField(Address, related_name='user_addresses')
    phones = models.ManyToManyField(Phone, related_name='user_phones')
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE, related_name='user_profession')
    user_type = models.IntegerField(_('Status'), choices=USER_TYPE_CHOICES, default=None)
    birth_country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='birth_country')
    actual_country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='actual_country')
    actual_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='actual_city')

    class Meta:
        verbose_name = _('User Data')
        verbose_name_plural = _('Users Data')
        db_table = 'user_data'
