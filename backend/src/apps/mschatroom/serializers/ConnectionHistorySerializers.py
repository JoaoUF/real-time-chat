from rest_framework import serializers
from mschatroom.models import ConnectionHistory


class ConnectionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectionHistory
        fields = "__all__"
