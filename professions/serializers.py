from rest_framework import serializers
from professions.models import Profession


class ProfessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profession
        fields = [
            'id',
            'title',
            # 'slug',
            'status',
            ]

    @staticmethod
    def load_queryset():
        queryset = Profession.objects.all()
        return queryset.distinct().order_by('title')
