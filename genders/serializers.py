from rest_framework import serializers
from genders.models import Gender


class GenderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gender
        fields = [
            'id',
            'title',
            'slug',
            'status',
            ]

    @staticmethod
    def load_queryset():
        queryset = Gender.objects.all()
        return queryset.distinct().order_by('title')
