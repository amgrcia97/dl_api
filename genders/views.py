from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from genders.models import Gender
from genders.serializers import GenderSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django_filters import rest_framework as filters
from rest_framework import filters as rest_framework_filters


class GenderAdminViewSet(viewsets.ModelViewSet):
    '''API for "Discere Linguis" Genders'''
    serializer_class = GenderSerializer
    permission_classes = (IsAdminUser, IsAuthenticated)
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
        gender = get_object_or_404(Gender.objects.filter(pk=pk))
        serializer = GenderSerializer(gender, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        gender = get_object_or_404(Gender.objects.filter(pk=pk))
        serializer = self.get_serializer(gender, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        gender = get_object_or_404(Gender.objects.filter(pk=pk))
        if gender.slug in ['male', 'female', 'none']:
            gender.status = 3
            gender.save()
        else:
            gender.delete()
        return Response({'deleted': gender.slug}, status=status.HTTP_202_ACCEPTED)

    @action(detail=False, methods=['GET'], name='Default genders registration', url_name='set-default-genders')
    def set_default_genders(self, request):
        from genders.signals import create_default_genders
        try:
            create_default_genders()
            return Response({'default_genders_installed': True}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({'default_genders_installed': False}, status=status.HTTP_406_NOT_ACCEPTABLE)
