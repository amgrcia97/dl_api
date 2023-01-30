from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from languages.models import Language
from languages.serializers import LanguageSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters import rest_framework as filters
from rest_framework import filters as rest_framework_filters


class LanguageAdminViewSet(viewsets.ModelViewSet):
    '''API for "Discere Linguis" Languages'''
    serializer_class = LanguageSerializer
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
        language = get_object_or_404(Language.objects.filter(pk=pk))
        serializer = LanguageSerializer(language, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        language = get_object_or_404(Language.objects.filter(pk=pk))
        serializer = self.get_serializer(language, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        language = get_object_or_404(Language.objects.filter(pk=pk))
        language.status = 3
        language.save()
        return Response({'deleted': language.title}, status=status.HTTP_202_ACCEPTED)

    @action(detail=False, methods=['GET'], name='Default languages registration', url_name='set-default-languages')
    def set_default_languages(self, request):
        from languages.signals import create_default_languages
        try:
            create_default_languages()
            return Response({'default_languages_installed': True}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({'default_languages_installed': False}, status=status.HTTP_406_NOT_ACCEPTABLE)
