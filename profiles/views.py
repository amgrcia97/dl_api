from rest_framework import viewsets  # , status
# from rest_framework.response import Response
from profiles.models import Profile
from profiles.serializers import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    '''API for Discere Linguis Profiles'''
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
