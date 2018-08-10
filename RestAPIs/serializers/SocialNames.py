from rest_framework import serializers

from BackendApp.models import SocialNames


class SocialNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialNames
        fields = ('id', 'name')
