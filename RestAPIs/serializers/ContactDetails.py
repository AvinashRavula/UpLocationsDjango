from rest_framework import serializers

from BackendApp.models import ContactDetails


class ContactDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactDetails
        fields = ('id', 'phone_numbers', 'email_ids', 'social_contacts')
