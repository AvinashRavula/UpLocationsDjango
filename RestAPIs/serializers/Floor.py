from rest_framework import serializers

from BackendApp.models import EmailIds, Floor


class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = ('id', 'venue', 'table')
