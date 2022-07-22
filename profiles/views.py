from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from profiles.models import Profile
from profiles.serializers import ProfileSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class ProfileAdminViewSet(viewsets.ModelViewSet):
    '''API for "Discere Linguis" Profiles'''
    queryset = Profile.objects.all().order_by('id')
    serializer_class = ProfileSerializer
    permission_classes = (IsAdminUser, IsAuthenticated)
    filterset_fields = ('id', 'title',)

    def get_queryset(self):
        return self.get_serializer().load_queryset()

    def create(self, request, pk=None):
        serializer = self.get_serializer(data=request.data, partial=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def retrieve(self, request, pk):
        profile = get_object_or_404(Profile.objects.filter(pk=pk))
        serializer = ProfileSerializer(profile, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        profile = get_object_or_404(Profile.objects.filter(pk=pk))
        serializer = self.get_serializer(profile, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        profile = get_object_or_404(Profile.objects.filter(pk=pk))
        profile.status = 3
        profile.save()
        return Response({'detail': 'deleted'}, status=status.HTTP_202_ACCEPTED)

    @action(detail=False, methods=['GET'], url_name='read-user-data')
    def set_default_profiles(self, request):
        from profiles.signals import create_default_profiles
        try:
            create_default_profiles()
            return Response({'default_profiles_installed': True}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({'default_profiles_installed': False}, status=status.HTTP_406_NOT_ACCEPTABLE)
