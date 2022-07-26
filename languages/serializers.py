from rest_framework import serializers
from languages.models import Language, CountryLanguage


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


class CountryLanguageSerializer(serializers.ModelSerializer):

    language = LanguageSerializer(many=True, read_only=True)

    class Meta:
        model = CountryLanguage
        fields = [
            'id',
            'title',
            'country',
            'language',
            'code',
            'status',
            ]

    @staticmethod
    def load_queryset():
        queryset = CountryLanguage.objects.all()
        return queryset.distinct().order_by('title')
