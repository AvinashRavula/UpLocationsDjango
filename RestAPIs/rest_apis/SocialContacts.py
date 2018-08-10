from rest_framework import viewsets

from BackendApp.models import SocialContacts
from RestAPIs.serializers.SocialContacts import SocialContactsSerializer


class SocialContactsViewSet(viewsets.ModelViewSet):
    queryset = SocialContacts.objects.all()
    serializer_class = SocialContactsSerializer
