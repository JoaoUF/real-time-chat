from msauthentication.models import CustomUser
from rest_framework import serializers


class CustomSerializerIdEmailFullName(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "email", "first_name", "last_name"]
