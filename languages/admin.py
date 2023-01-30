from django.contrib import admin
from languages.models import Language


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'code',
        'status'
        )


# @admin.register(CountryLanguage)
# class CountryLanguageAdmin(admin.ModelAdmin):
#     list_display = (
#         'id',
#         'title',
#         'country',
#         'language',
#         'code',
#         'status'
#         )
