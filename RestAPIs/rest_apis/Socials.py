from rest_framework import viewsets

from BackendApp.models import Socials
from RestAPIs.serializers.Socials import SocialsSerializer


class SocialsViewSet(viewsets.ModelViewSet):
    queryset = Socials.objects.all()
    serializer_class = SocialsSerializer
