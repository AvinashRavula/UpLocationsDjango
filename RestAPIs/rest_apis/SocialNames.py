from rest_framework import viewsets

from BackendApp.models import SocialNames
from RestAPIs.serializers.SocialNames import SocialNamesSerializer


class SocialNamesViewSet(viewsets.ModelViewSet):
    queryset = SocialNames.objects.all()
    serializer_class = SocialNamesSerializer
