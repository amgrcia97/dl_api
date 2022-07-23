from django.contrib import admin
from addresses.models import State, City, Address


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'country',
        'status'
        )


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'state',
        'status'
        )


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'address',
        'number',
        'neighborhood',
        'city'
        )
