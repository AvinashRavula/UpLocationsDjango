from rest_framework import viewsets

from BackendApp.models import Venues
from RestAPIs.serializers.Venues import VenuesSerializer


class VenuesViewSet(viewsets.ModelViewSet):
    queryset = Venues.objects.all()
    serializer_class = VenuesSerializer
