from rest_framework import serializers

from BackendApp.models import PhoneNumbers


class PhoneNumbersSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumbers
        fields = ('id', 'phone_number')
