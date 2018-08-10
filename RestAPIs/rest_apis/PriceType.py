from rest_framework import viewsets

from BackendApp.models import PriceType
from RestAPIs.serializers.PriceType import PriceTypeSerializer


class PriceTypeViewSet(viewsets.ModelViewSet):
    queryset = PriceType.objects.all()
    serializer_class = PriceTypeSerializer
