from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from accounts.managers import UserManager
from addresses.models import Country, State, City, Address


DEFAULT_STATUS = (
        (1, _('Active')),
        (2, _('Inactive')),
        (3, _('Deleted')),
    )


class User(AbstractBaseUser, PermissionsMixin):
    '''User'''
    full_name = models.CharField(_('Name'), max_length=255, null=False, blank=False)
    email = models.EmailField(_('Email'), blank=False, unique=True)
    nick_name = models.CharField(_('Nickname'), max_length=255, null=True, blank=True, default=None)
    date_joined = models.DateTimeField(_('Date Joined'), auto_now_add=True)
    date_updated = models.DateTimeField(_('Date Changed'), auto_now=True)
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


class UserAvatar(models.Model):
    '''User Image'''
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='user_avatar')
    image = models.CharField(_('Imagem'), max_length=1024, null=False, blank=False)

    class Meta:
        verbose_name = _('User Avatar')
        verbose_name_plural = _('Users Avatars')
        db_table = 'users_avatars'


class UserData(models.Model):
    USER_TYPE = (
        (1, _('Teacher')),
        (2, _('Student')),
        (3, _('Admin_Master')),
    )
    USER_GENDER = (
        (1, _('Male')),
        (2, _('Female')),
        (3, _('Other')),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='user_data')
    type = models.IntegerField(_('User Type'), choices=USER_TYPE, null=False, default=2)
    age = models.IntegerField(_('User Age'), null=True)
    phone = models.CharField(_('Phone'), max_length=126, null=True, blank=False)
    gender = models.IntegerField(_('User Gender'), choices=USER_GENDER, null=True)
    birthday = models.DateField(_('Data de nascimento'), auto_now=False, null=True)
    document = models.CharField(_('Documento'), max_length=255, blank=True, null=True, unique=True)
    born_country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='user_born_country')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='user_country')
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='user_state')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='user_city')
    addresses = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='user_addresses')

    class Meta:
        verbose_name = _('Dados do usuário')
        verbose_name_plural = _('Dados dos usuários')
        db_table = 'user_data'
