from django.contrib import admin
from accounts.models import (
    User
)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'full_name',
        'email',
        'nick_name',
        'date_joined',
        'date_updated',
        'status',
        'is_staff',
        'is_superuser'
        )
