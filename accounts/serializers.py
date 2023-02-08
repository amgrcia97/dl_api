from rest_framework import serializers
from accounts.models import User, UserData


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = [
            'type',
            'phone',
            'gender',
            'birthday',
            'document',
            'born_country',
            'born_language',
            'country',
            'state',
            'city',
            'interest_language',
            'address',
        ]


class UsersSerializer(serializers.ModelSerializer):
    image = serializers.CharField(source='user_avatar.image')
    user_data = UserDataSerializer()

    class Meta:
        model = User
        fields = [
            'id',
            'full_name',
            'nick_name',
            'email',
            'date_joined',
            'date_updated',
            'is_staff',
            'is_superuser',
            'image',
            'user_data'
        ]
