from rest_framework import serializers
# from rest_framework.exceptions import ValidationError
# from django.utils.translation import gettext_lazy as _
from accounts.models import (
    User,
    UserData
)


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class UserDataSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='user_id', read_only=True)
    full_name = serializers.CharField(source='user.full_name')
    email = serializers.CharField(source='user.email')
    date_joined = serializers.DateTimeField(source='user.date_joined', read_only=True)
    date_updated = serializers.DateTimeField(source='user.date_updated', read_only=True)
    status = serializers.IntegerField(source='user.status')

    class Meta:
        model = UserData
        fields = [
            'id',
            'full_name',
            'email',
            'date_joined',
            'date_updated',
            'status',
            'type',
            'age',
            'phone',
            'gender',
            'birthday',
            'document',
            'born_country',
            'country',
            'state',
            'city',
            'born_language',
            'interest_language',
            'address',
        ]
        required_fields = [
            'id',
            'full_name',
            'email',
            'date_joined',
            'date_updated',
            'status',
            'type',
            'age',
            'phone',
            'gender',
            'birthday',
            'document',
            'born_country',
            'country',
            'state',
            'city',
            'born_language',
            'interest_language',
            'address'
            ]

    def validate(self, data):
        # # 'id',
        # # 'full_name',
        # print('data->', data)
        # user = data.get('user', None)
        # # print(dir(data))
        # # print(data.keys())
        # print('user->', user)
        # if len(full_name.split(' ')) <= 1:
        #     raise ValidationError({'full_name': _('Informe seu nome e sobrenome')})
        # 'email',
        # 'date_joined',
        # 'date_updated',
        # 'status',
        # 'type',
        # 'age',
        # 'phone',
        # 'gender',
        # 'birthday',
        # 'document',
        # 'born_country',
        # 'country',
        # 'state',
        # 'city',
        # 'born_language',
        # 'interest_language',
        # 'address'
        # interest_language = data.get('interest_language', None)
        # if interest_language is None:
        #     raise ValidationError({'interest_language': _('interest_language não pode ser vazio ou nulo')})
        # print('validate->', data)
        # raise ValidationError('Não criado')
        return data

    def create(self, validated_data):
        # extra_data, validated_data = self._get_data(validated_data)
        # if extra_data['areas'] is None:
        #     raise ValidationError({'areas': _('Areas não definidas')})
        # instance = LiveClass.objects.create(**validated_data)
        # instance.live_class_google_firebase()
        # return self._save_live_class_data(instance, extra_data)
        print('create->', validated_data)
        return validated_data

    def update(self, instance, validated_data):
        # extra_data, validated_data = self._get_data(validated_data)
        # list_participants = validated_data.pop('list_participants', None)
        # instance.title = validated_data.get('title', instance.title)
        # instance.code = validated_data.get('code', instance.code)
        # instance.description = validated_data.get('description', instance.description)
        # instance.date_class = validated_data.get('date_class', instance.date_class)
        # instance.timezone = validated_data.get('timezone', instance.timezone)
        # instance.type = validated_data.get('type', instance.type)
        # instance.live_class_type = validated_data.get('live_class_type', instance.live_class_type)
        # instance.platform_type = validated_data.get('platform_type', instance.platform_type)
        # instance.embed = validated_data.get('embed', instance.embed)
        # instance.qty_limit_participants = validated_data.get('qty_limit_participants', instance.description)
        # instance.status = validated_data.get('status', instance.status)
        # instance.score = validated_data.get('score', instance.score)
        # instance.workload = validated_data.get('workload', instance.workload)
        # instance.unpublish_date = validated_data.get('unpublish_date', instance.unpublish_date)
        # instance.save()
        # instance.live_class_google_firebase()
        # instance = self._save_live_class_data(instance, extra_data)
        # if instance.status == 1:
        #     LiveClass.objects.schedule_email_notifications_event(live_class=instance)

        # if instance.status == 4 and list_participants is not None:
        #     LiveClass.objects.check_user_result(list_participants, instance)
        print('create->', instance, validated_data)
        return instance
