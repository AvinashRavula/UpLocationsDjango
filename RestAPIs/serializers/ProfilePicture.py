from rest_framework import serializers

from BackendApp.models import ProfilePicture


class ProfilePictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfilePicture
        fields = ('id', 'link')