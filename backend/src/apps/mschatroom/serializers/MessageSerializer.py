from mschatroom.models import Message
from rest_framework import serializers


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"


class MessageSerializerLastMessage(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["content", "sent_at", "seen"]
