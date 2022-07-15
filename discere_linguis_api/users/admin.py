from django.contrib import admin
# from .models import (
#     Country,
#     State,
#     City,
#     Address,
#     User,
#     AgeGroup,
#     Gender,
#     Phone,
#     Profession,
#     UserData
#     )


# @admin.register(Country)
# class CountryAdmin(admin.ModelAdmin):
#     list_display = ('name',)


# @admin.register(State)
# class StateAdmin(admin.ModelAdmin):
#     list_display = ('name')


# @admin.register(City)
# class CityAdmin(admin.ModelAdmin):
#     list_display = ('address', 'number', 'complement', 'neighborhood', 'city', 'postal_code')


# @admin.register(Address)
# class AddressAdmin(admin.ModelAdmin):
#     list_display = ('address', 'number', 'complement', 'neighborhood', 'city', 'postal_code')


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('full_name', 'email', 'date_joined', 'is_superuser')


# @admin.register(AgeGroup)
# class AgeGroupAdmin(admin.ModelAdmin):
#     list_display = ('title', 'slug', 'status')


# @admin.register(Gender)
# class GenderAdmin(admin.ModelAdmin):
#     list_display = ('title')


# @admin.register(Phone)
# class PhoneAdmin(admin.ModelAdmin):
#     list_display = ('phone')


# @admin.register(Profession)
# class ProfessionAdmin(admin.ModelAdmin):
#     list_display = ('profession')


# @admin.register(UserData)
# class UserDataAdmin(admin.ModelAdmin):
#     list_display = (
#         'profession', 'user', 'gender', 'age_group', 'birthday', 'document',
#         'addresses', 'phones', 'profession', 'user_type', 'birth_country',
#         'actual_country', 'actual_city')
