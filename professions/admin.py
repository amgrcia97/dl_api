from django.contrib import admin
from professions.models import Profession


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        # 'slug',
        'status'
        )
