from rest_framework import viewsets

from BackendApp.models import ContactDetails
from RestAPIs.serializers.ContactDetails import ContactDetailsSerializer


class ContactDetailsViewSet(viewsets.ModelViewSet):
    queryset = ContactDetails.objects.all()
    serializer_class = ContactDetailsSerializer
