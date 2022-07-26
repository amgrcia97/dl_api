from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from countries.models import Country
from countries.serializers import CountrySerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django_filters import rest_framework as filters
from rest_framework import filters as rest_framework_filters


class CountryAdminViewSet(viewsets.ModelViewSet):
    '''API for "Discere Linguis" Countries'''
    serializer_class = CountrySerializer
    permission_classes = (IsAdminUser, IsAuthenticated)
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.SearchFilter,
        rest_framework_filters.OrderingFilter,
    )
    filterset_fields = ('id', 'name')
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
        country = get_object_or_404(Country.objects.filter(pk=pk))
        serializer = CountrySerializer(country, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        country = get_object_or_404(Country.objects.filter(pk=pk))
        serializer = self.get_serializer(country, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        country = get_object_or_404(Country.objects.filter(pk=pk))
        country.status = 3
        country.save()
        return Response({'deleted': country.title}, status=status.HTTP_202_ACCEPTED)

    @action(detail=False, methods=['GET'], name='Default countries registration', url_name='set-default-countries')
    def set_default_countries(self, request):
        from countries.signals import create_default_countries
        try:
            create_default_countries()
            return Response({'default_countries_installed': True}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({'default_countries_installed': False}, status=status.HTTP_406_NOT_ACCEPTABLE)
