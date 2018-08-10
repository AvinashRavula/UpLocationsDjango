from rest_framework import viewsets

from BackendApp.models import EmailIds, Floor
from RestAPIs.serializers.EmailIds import EmailIdsSerializer
from RestAPIs.serializers.Floor import FloorSerializer


class FloorViewSet(viewsets.ModelViewSet):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer
