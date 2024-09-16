from msauthentication.models import CustomUser
from msauthentication.serializers import CustomUserSerializerIdEmailFullName
from rest_framework import generics


class CustomUserListAvailable(generics.ListAPIView):
    queryset = CustomUser.objects.values("id", "email")
    serializer_class = CustomUserSerializerIdEmailFullName
