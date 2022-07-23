from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from professions.models import Profession
from professions.serializers import ProfessionSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters import rest_framework as filters
from rest_framework import filters as rest_framework_filters


class ProfessionAdminViewSet(viewsets.ModelViewSet):
    '''API for "Discere Linguis" Professions'''
    serializer_class = ProfessionSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.SearchFilter,
        rest_framework_filters.OrderingFilter,
    )
    filterset_fields = ('id', 'title')
    search_fields = filterset_fields
    ordering_fields = search_fields

    def get_queryset(self):
        return self.get_serializer().load_queryset()

    def create(self, request, pk=None):
        serializer = self.get_serializer(data=request.data, partial=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def retrieve(self, request, pk):
        profession = get_object_or_404(Profession.objects.filter(pk=pk))
        serializer = ProfessionSerializer(profession, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        profession = get_object_or_404(Profession.objects.filter(pk=pk))
        serializer = self.get_serializer(profession, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        profession = get_object_or_404(Profession.objects.filter(pk=pk))
        profession.status = 3
        profession.save()
        return Response({'deleted': profession.title}, status=status.HTTP_202_ACCEPTED)

    @action(detail=False, methods=['GET'], name='Default profession registration', url_name='set-default-professions')
    def set_default_professions(self, request):
        from professions.signals import create_default_professions
        try:
            create_default_professions()
            return Response({'default_professions_installed': True}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({'default_professions_installed': False}, status=status.HTTP_406_NOT_ACCEPTABLE)
