from rest_framework import serializers

from BackendApp.models import EmailIds


class EmailIdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailIds
        fields = ('id', 'email_id')