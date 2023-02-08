from rest_framework import serializers
from rest_framework.serializers import ValidationError
from accounts.models import User, UserData
from addresses.models import Country
from languages.models import CountryLanguage, Language


class EmptySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = []


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
    image = serializers.CharField(source='user_avatar.image', read_only=True)
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

    def validate(self, data):
        user_data = data.get('user_data', None)
        if data.get('user_data', None) in [None, '']:
            raise ValidationError({'user_data': 'Please provida the user data'})
        if user_data.get('type', None) is None:
            raise ValidationError({'user_type': 'Please inform a user type'})
        if user_data.get('phone', None) is None:
            raise ValidationError({'phone': 'Please inform a phone'})
        if user_data.get('gender', None) is None:
            raise ValidationError({'gender': 'Please inform a gender'})
        if user_data.get('birthday', None) is None:
            raise ValidationError({'birthday': 'Please inform a birthday'})
        if user_data.get('born_country', None) is None:
            raise ValidationError({'born_country': 'Please inform a born country'})
        if user_data.get('born_language', None) is None:
            raise ValidationError({'born_language': 'Please inform a born language'})
        if user_data.get('country', None) is None:
            raise ValidationError({'country': 'Please inform your actual country'})
        if user_data.get('interest_language', None) is None:
            raise ValidationError({'interest_language': 'Please inform an interest language'})
        # TODO: adicionar validação de documento, state, city, address e endereço no futuro user_data.get('document', None)
        if user_data.get('type', None) == 2:
            if user_data.get('interest_language', None) == Language.objects.filter(country_language_language=user_data.get('born_language', None)).first():
                raise ValidationError({'Languages': 'Born language and interest language can not be the same for an student'})
        return data

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        confirm_password = validated_data.pop('confirm_password', None)
        if password is None or confirm_password is None:
            raise ValidationError({'password': 'Please inform a password and confirm it'})
        if password != confirm_password:
            raise ValidationError({'password': 'Passwords does not match'})
        if User.objects.filter(email=validated_data.get('email', None)):
            raise ValidationError({'email': 'Informed email already exists'})
        user_data = validated_data.pop('user_data', None)
        # Grava o usuário
        user = User.objects.create(**validated_data)
        if password:
            user.set_password(password)
            user.save()
        if not UserData.objects.filter(user__email=validated_data.get('email', None)).exists():
            serializer_user_data = UserDataSerializer(data=user_data, partial=True)
            if serializer_user_data.is_valid(raise_exception=True):
                UserData.objects.create(
                    user=user,
                    type=user_data.get('type', None),
                    phone=user_data.get('phone', None),
                    gender=user_data.get('gender', None),
                    birthday=user_data.get('birthday', None),
                    document=user_data.get('document', None),
                    born_country=Country.objects.get(id=user_data.get('born_country', None)),
                    born_language=CountryLanguage.objects.get(id=user_data.get('born_language', None)),
                    country=Country.objects.get(id=user_data.get('country', None)),
                    # state=Country.objects.get(id=user_data.get('state', None)),
                    # city=Country.objects.get(id=user_data.get('city', None)),
                    interest_language=Language.objects.get(id=user_data.get('interest_language', None)),
                    # instance.user_data.address = Address.objects.get(id=user_data.get('address', None))
                )
        return user
