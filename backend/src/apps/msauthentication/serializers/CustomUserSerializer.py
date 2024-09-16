from msauthentication.models import CustomUser
from rest_framework import serializers


class CustomUserSerializerIdEmailFullName(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "email"]
