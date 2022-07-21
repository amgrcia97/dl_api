from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Creates and saves a User with the given email and password"""
        from accounts.models import User
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        email = email.lower()
        extra_fields['date_joined'] = timezone.now() if 'date_joined' not in extra_fields else extra_fields['date_joined']
        extra_fields['date_updated'] = timezone.now() if 'date_updated' not in extra_fields else extra_fields['date_updated']

        user = User.objects.filter(email=email)

        if user.count() == 0:
            user = User(email=email, **extra_fields)
            user.set_password(password)
            user.save()
        else:
            user = user.get()
            user.full_name = extra_fields['full_name']
            user.email = email
            user.set_password(password)
            user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        return self._create_user(email, password, **extra_fields)
