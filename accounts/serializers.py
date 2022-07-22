from rest_framework import serializers
from accounts.models import (
    User,
    UserImage,
    AgeGroup,
    Phone,
    UserType,
    UserData
)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = User
        fields = [
            'id',
            'username',
            'nick_name',
            'date_joined',
            'date_updated',
            'status',
            'is_staff',
            'is_superuser'
        ]


class UserImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserImage
        fields = [
            'user',
            'image',
        ]


class AgeGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = AgeGroup
        fields = [
            'title',
            'slug',
            'status'
        ]


class PhoneSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'phone': {'write_only': True}
        }
        model = Phone
        fields = [
            'phone'
        ]


class UserTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserType
        fields = [
            'title',
            'slug',
            'status'
        ]


class UserDataSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'document': {'write_only': True},
            'address': {'write_only': True},
        }
        model = UserData
        fields = [
            'user',
            'gender',
            'age_group',
            'birthday',
            'document',
            'address',
            'phone',
            'profession',
            'user_type',
            'profile'
        ]
