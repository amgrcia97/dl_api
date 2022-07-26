from rest_framework import serializers
from countries.models import Country


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = [
            'id',
            'name',
            'code',
            'status',
            ]

    @staticmethod
    def load_queryset():
        queryset = Country.objects.all()
        return queryset.distinct().order_by('name')
