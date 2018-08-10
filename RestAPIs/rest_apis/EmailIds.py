from rest_framework import viewsets

from BackendApp.models import EmailIds
from RestAPIs.serializers.EmailIds import EmailIdsSerializer


class EmailIdsViewSet(viewsets.ModelViewSet):
    queryset = EmailIds.objects.all()
    serializer_class = EmailIdsSerializer
