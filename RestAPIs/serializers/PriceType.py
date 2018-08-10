from rest_framework import serializers

from BackendApp.models import PriceType


class PriceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceType
        fields = ('id', 'type')
