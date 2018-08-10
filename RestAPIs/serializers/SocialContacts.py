from rest_framework import serializers

from BackendApp.models import SocialContacts


class SocialContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialContacts
        fields = ('id', 'links')
