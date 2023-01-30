from rest_framework import viewsets  # , status
# from rest_framework.response import Response
from accounts.models import (
    User
)
from accounts.serializers import (
    UserSerializer
)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    '''API for Discere Linguis Users'''
    queryset = User.objects.all()
    serializer_class = UserSerializer
