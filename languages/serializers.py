from rest_framework import serializers
from languages.models import Language


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = [
            'id',
            'title',
            'code',
            'status',
            ]

    @staticmethod
    def load_queryset():
        queryset = Language.objects.all()
        return queryset.distinct().order_by('title')
