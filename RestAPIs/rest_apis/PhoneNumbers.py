from rest_framework import viewsets

from BackendApp.models import PhoneNumbers
from RestAPIs.serializers.PhoneNumbers import PhoneNumbersSerializer


class PhoneNumbersViewSet(viewsets.ModelViewSet):
    queryset = PhoneNumbers.objects.all()
    serializer_class = PhoneNumbersSerializer
