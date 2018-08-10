from rest_framework import serializers

from BackendApp.models import EmailIds, Table


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ('id', 'table_no', 'no_of_seats', 'booked', 'user')
