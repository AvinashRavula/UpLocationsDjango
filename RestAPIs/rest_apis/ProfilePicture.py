from rest_framework import viewsets

from BackendApp.models import ProfilePicture
from RestAPIs.serializers.ProfilePicture import ProfilePictureSerializer


class ProfilePictureViewSet(viewsets.ModelViewSet):
    queryset = ProfilePicture.objects.all()
    serializer_class = ProfilePictureSerializer
