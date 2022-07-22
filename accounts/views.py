from rest_framework import viewsets  # , status
# from rest_framework.response import Response
from accounts.models import (
    User,
    UserData
)
from accounts.serializers import (
    UserDataSerializer,
    UserSerializer
)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    '''API for Discere Linguis Users'''
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDataViewSet(viewsets.ModelViewSet):
    '''API for Discere Linguis Users'''
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer
