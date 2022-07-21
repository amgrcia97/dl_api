from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from accounts.managers import UserManager

DEFAULT_STATUS = (
        (1, _('Active')),
        (2, _('Inactive')),
        (3, _('Deleted')),
    )


class User(AbstractBaseUser, PermissionsMixin):
    '''User'''
    username = models.CharField(_('Name'), max_length=255, null=False, blank=False)
    email = models.EmailField(_('Email'), blank=False, unique=True)
    nick_name = models.CharField(_('Nickname'), max_length=255, null=True, blank=True, default=None)
    date_joined = models.DateTimeField(_('Date Joined'), auto_now_add=False)
    date_updated = models.DateTimeField(_('Date Changed'), auto_now=False)
    status = models.IntegerField(_('Status'), choices=DEFAULT_STATUS, default=2)
    is_staff = models.BooleanField(_('is_staff'), default=False)
    is_superuser = models.BooleanField(_('is_superuser'), default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        db_table = 'users'


class UserImage(models.Model):
    '''User Image'''
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='user_image')
    image = models.CharField(_('Imagem'), max_length=1024, null=False, blank=False)

    class Meta:
        verbose_name = _('User Image')
        verbose_name_plural = _('Users Images')
        db_table = 'users_images'


class Gender(models.Model):
    '''Gender'''
    title = models.CharField(_('Gender'), max_length=255, blank=False, null=False)
    slug = models.SlugField(_('Slug'), unique=True)

    class Meta:
        verbose_name = _('Gender')
        verbose_name_plural = _('Genders')
        db_table = 'genders'


class AgeGroup(models.Model):
    '''AgeGroup'''
    title = models.CharField(_('Title'), max_length=120, null=False, blank=False)
    slug = models.SlugField(_('Slug'), blank=False, null=False, unique=True)
    status = models.IntegerField(_('Status'), choices=DEFAULT_STATUS, default=1)

    class Meta:
        verbose_name = _('AgeGroup')
        verbose_name_plural = _('AgeGroups')
        db_table = 'age_groups'


class Country(models.Model):
    '''Country'''
    name = models.CharField(_('Country'), max_length=256, null=False, blank=False)

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')
        db_table = 'countries'


class State(models.Model):
    '''State'''
    name = models.CharField(_('State'), max_length=256, null=False, blank=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country_states')

    class Meta:
        verbose_name = _('State')
        verbose_name_plural = _('States')
        db_table = 'states'


class City(models.Model):
    '''City'''
    name = models.CharField(_('City'), max_length=256, null=False, blank=False)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='state_cities')

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


class Phone(models.Model):
    '''Phone'''
    phone = models.CharField(_('Phone'), max_length=126, blank=False, null=False)

    class Meta:
        verbose_name = _('Phone')
        verbose_name_plural = _('Phones')
        db_table = 'phones'


class Profession(models.Model):
    '''Profession'''
    title = models.CharField(_('Profession'), max_length=255, blank=False, null=False)
    slug = models.SlugField(_('slug'), unique=True, blank=False, null=False)
    status = models.IntegerField(_('Status'), choices=DEFAULT_STATUS, default=1)

    class Meta:
        verbose_name = _('Profession')
        verbose_name_plural = _('Professions')
        db_table = 'professions'


class UserType(models.Model):
    '''User Type'''
    title = models.CharField(_('User Type'), max_length=255, blank=False, null=False)
    slug = models.SlugField(_('slug'), unique=True, blank=False, null=False)
    status = models.IntegerField(_('Status'), choices=DEFAULT_STATUS, default=1)

    class Meta:
        verbose_name = _('User Type')
        verbose_name_plural = _('User Types')
        db_table = 'user_types'


class Profile(models.Model):
    '''Profile'''
    title = models.CharField(_('Profile'), max_length=255, blank=False, null=False)
    slug = models.SlugField(_('slug'), unique=True, blank=False, null=False)
    status = models.IntegerField(_('Status'), choices=DEFAULT_STATUS, default=1)

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')
        db_table = 'profiles'


class UserData(models.Model):
    '''User Data'''
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='user_data')
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, related_name='user_gender', null=True)
    age_group = models.ForeignKey(AgeGroup, on_delete=models.CASCADE, related_name='user_age_group', null=True)
    birthday = models.DateField(_('Data de nascimento'), auto_now=False, null=True)
    document = models.CharField(_('Documento'), max_length=255, blank=True, null=True, unique=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='user_address', null=True)
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE, related_name='user_phone', null=True)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE, related_name='user_profession', null=True)
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE, related_name='user_type', null=True, default=None)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile', null=True, default=None)

    class Meta:
        verbose_name = _('User Data')
        verbose_name_plural = _('Users data')
        db_table = 'users_data'
