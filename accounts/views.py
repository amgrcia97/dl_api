from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from accounts.models import User, UserData
from addresses.models import Country, State, City
from languages.models import Language
from accounts.serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    '''API for Discere Linguis Users'''
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EmptySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = []


class RegisterUserView(viewsets.GenericViewSet):
    '''User register methods'''
    serializer_class = EmptySerializer

    @action(detail=False, methods=['GET'], name='Pre-register Lists')
    def get_register_lists(self, request):
        data = {
            'genders': dict(UserData.USER_GENDER),
            'countries': Country.objects.filter(status=1),
            'states': State.objects.filter(status=1),
            'cities': City.objects.filter(status=1),
            'languages': Language.objects.filter(status=1),
        }
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST'], name='Check if the informed document already exists')
    def check_user_document_existance(self, request):
        if not request.data.get('document', None):
            raise ValidationError({'document': _('Please inform a document')})
        document = request.data.get('document')
        exists = UserData.objects.filter(document=document).exists()
        if exists:
            return Response('Document already exist', status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response('Valid document', status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST'], name='Check if the informed email already exists')
    def check_user_email_existance(self, request):
        if not request.data.get('email', None):
            raise ValidationError({'email': _('Please inform a document')})
        email = request.data.get('email')
        exist = User.objects.filter(email=email).exists()
        if exist:
            return Response('Email already exist', status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response('Valid email', status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST'], name='Solicita a gravação de um usuário')
    def pre_register_student(self, request):
        '''Solicita a criação de um usuário e fica no aguardo da confirmação do email'''
        return Response('Método não implementado', status=status.HTTP_501_NOT_IMPLEMENTED)

    @action(detail=False, methods=['POST'], name='Solicita a gravação de um usuário')
    def pre_register_teacher(self, request):
        '''Solicita a criação de um usuário e fica no aguardo da confirmação do email'''
        return Response('Método não implementado', status=status.HTTP_501_NOT_IMPLEMENTED)

    @action(detail=False, methods=['POST'], name='Solicita a gravação de um usuário')
    def register_student(self, request):
        '''Recebe o código de confrimação do email e muda o status do usuário para activo'''
        return Response('Método não implementado', status=status.HTTP_501_NOT_IMPLEMENTED)

    @action(detail=False, methods=['POST'], name='Solicita a gravação de um usuário')
    def register_user(self, request):
        '''Recebe o código de confrimação do email e muda o status do usuário para activo'''
        return Response('Método não implementado', status=status.HTTP_501_NOT_IMPLEMENTED)

    @action(detail=False, methods=['POST'], url_name='user-accept-terms-and-conditions', permission_classes=[IsAuthenticated])
    def user_accept_terms_and_conditions(self, request):
        '''Criação ou atualização do aceite dos termos e condições pelo usuário'''
        return Response('Método não implementado', status=status.HTTP_501_NOT_IMPLEMENTED)
