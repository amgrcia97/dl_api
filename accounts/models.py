from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from accounts.managers import UserManager
from addresses.models import Address
from countries.models import Country, CountryLanguage
from genders.models import Gender
from languages.models import Language
from professions.models import Profession
from profiles.models import Profile


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
    status = models.IntegerField(_('Status'), choices=DEFAULT_STATUS, default=1)
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


class AgeGroup(models.Model):
    '''AgeGroup'''
    title = models.CharField(_('Title'), max_length=120, null=False, blank=False)
    slug = models.SlugField(_('Slug'), blank=False, null=False, unique=True)
    status = models.IntegerField(_('Status'), choices=DEFAULT_STATUS, default=1)

    class Meta:
        verbose_name = _('AgeGroup')
        verbose_name_plural = _('AgeGroups')
        db_table = 'age_groups'


class Phone(models.Model):
    '''Phone'''
    phone = models.CharField(_('Phone'), max_length=126, blank=False, null=False)

    class Meta:
        verbose_name = _('Phone')
        verbose_name_plural = _('Phones')
        db_table = 'phones'


class UserType(models.Model):
    '''User Type'''
    USER_TYPE_STATUS = (
        (1, _('Active')),
        (2, _('Inactive')),
        (3, _('Deleted')),
    )
    title = models.CharField(_('User Type'), max_length=255, blank=False, null=False)
    slug = models.SlugField(_('slug'), unique=True, blank=False, null=False)
    status = models.IntegerField(_('Status'), choices=DEFAULT_STATUS, default=1)

    class Meta:
        verbose_name = _('User Type')
        verbose_name_plural = _('User Types')
        db_table = 'user_types'


class UserData(models.Model):
    '''User Data'''
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='user_data')
    born_country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='user_born_country')
    born_language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='user_born_language')
    interest_languages = models.ManyToManyField(CountryLanguage, related_name='interest_languages')
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, related_name='user_gender', null=True)
    age_group = models.ForeignKey(AgeGroup, on_delete=models.CASCADE, related_name='user_age_group', null=True)
    birthday = models.DateField(_('Data de nascimento'), auto_now=False, null=True)
    document = models.CharField(_('Documento'), max_length=255, blank=True, null=True, unique=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='user_address', null=True)
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE, related_name='user_phone', null=True)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE, related_name='user_profession', null=True)
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE, related_name='user_type', null=True, default=None)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user_profile', null=True)

    class Meta:
        verbose_name = _('User Data')
        verbose_name_plural = _('Users data')
        db_table = 'users_data'
