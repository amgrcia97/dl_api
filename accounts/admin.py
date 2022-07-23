from django.contrib import admin
from accounts.models import (
    User,
    AgeGroup,
    Phone,
    UserType,
    UserData
)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'email',
        'nick_name',
        'date_joined',
        'date_updated',
        'status',
        'is_staff',
        'is_superuser'
        )


@admin.register(AgeGroup)
class AgeGroupAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'slug',
        'status'
        )


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'phone',
        )


@admin.register(UserType)
class UserTypeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'slug',
        'status'
        )


@admin.register(UserData)
class UserDataAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'gender',
        'age_group',
        'birthday',
        'document',
        'address',
        'phone',
        'profession',
        'user_type'
        )
