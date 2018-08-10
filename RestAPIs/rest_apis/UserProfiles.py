from rest_framework import viewsets

from BackendApp.models import UserProfiles
from RestAPIs.serializers.UserProfiles import UserProfilesSerializer


class UserProfilesViewSet(viewsets.ModelViewSet):
    queryset = UserProfiles.objects.all()
    serializer_class = UserProfilesSerializer
