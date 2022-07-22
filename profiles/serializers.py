from rest_framework import serializers
from profiles.models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = [
            'id',
            'title',
            'slug',
            'status',
            ]

    @staticmethod
    def load_queryset():
        queryset = Profile.objects.all()
        return queryset.distinct().order_by('id')
