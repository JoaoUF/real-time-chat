from msauthentication.models import CustomUser
from msauthentication.serializers import CustomSerializerIdEmailFullName
from rest_framework import generics


class CustomUserListAvailable(generics.ListAPIView):
    queryset = CustomUser.objects.values("id", "email", "first_name", "last_name")
    serializer_class = CustomSerializerIdEmailFullName
