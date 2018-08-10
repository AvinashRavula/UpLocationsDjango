from rest_framework import serializers

from BackendApp.models import UserProfiles


class UserProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfiles
        fields = ('id', 'profile_picture', 'dob', 'gender')
