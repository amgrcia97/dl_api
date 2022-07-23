from django.contrib import admin
from genders.models import Gender


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'slug',
        'status'
        )
