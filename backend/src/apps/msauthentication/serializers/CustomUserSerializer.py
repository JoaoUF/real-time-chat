from msauthentication.models import CustomUser
from rest_framework import serializers
from mschatroom.models import ConnectionHistory


class CustomUserSerializerIdEmailFullName(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "email"]


class CustomUserSerializerBaseProfile(serializers.ModelSerializer):
    status = serializers.SerializerMethodField("get_status")
    full_name = serializers.SerializerMethodField("get_full_name")

    class Meta:
        model = CustomUser
        fields = ["id", "full_name", "email", "status"]

    def get_status(self, instance):
        return ConnectionHistory.objects.get(user=instance.id).status

    def get_full_name(self, instance):
        return instance.get_full_name
