from django.contrib import admin
from accounts.models import (
    User,
    Gender,
    AgeGroup,
    Country,
    State,
    City,
    Address,
    Phone,
    Profession,
    UserType,
    UserData
)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username', 'email', 'nick_name', 'date_joined', 'date_updated',
        'status', 'is_staff', 'is_superuser')


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')


@admin.register(AgeGroup)
class AgeGroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status')


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'state')


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('address', 'number', 'complement', 'neighborhood', 'city')


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('phone', )


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status')


@admin.register(UserType)
class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status')


@admin.register(UserData)
class UserDataAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'gender', 'age_group', 'birthday', 'document', 'address',
        'phone', 'profession', 'user_type')
