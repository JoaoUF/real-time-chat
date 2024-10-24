from msauthentication.models import CustomUser
from rest_framework import serializers
from mschatroom.models import ConnectionHistory


class CustomUserSerializerIdEmailFullName(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "email"]


class CustomUserSerializerBaseProfile(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ["id", "first_name", "last_name", "email", "status"]

    def get_status(self, obj):
        return ConnectionHistory.objects.get(user=obj.id).status
