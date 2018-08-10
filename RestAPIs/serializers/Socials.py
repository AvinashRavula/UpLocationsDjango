from rest_framework import serializers

from BackendApp.models import Socials


class SocialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socials
        fields = ('id', 'social_name', 'social_link')
