from rest_framework import serializers

from BackendApp.models import Venues


class VenuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venues
        fields = ('id', 'venue_name', 'address', 'latitude', 'longitude', 'price_type', 'contact')
