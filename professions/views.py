# from django.shortcuts import get_object_or_404
from rest_framework import viewsets  # , status
# from rest_framework.decorators import action
# from rest_framework.response import Response
from professions.models import Profession
from professions.serializers import ProfessionSerializer
from rest_framework.permissions import IsAuthenticated


class ProfessionAdminViewSet(viewsets.ModelViewSet):
    '''API for "Discere Linguis" Professions'''
    queryset = Profession.objects.all().order_by('id')
    serializer_class = ProfessionSerializer
    permission_classes = (IsAuthenticated)
    filterset_fields = ('title')
