from rest_framework import viewsets

from BackendApp.models import EmailIds, Table
from RestAPIs.serializers.EmailIds import EmailIdsSerializer
from RestAPIs.serializers.Table import TableSerializer


class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
