from mschatroom.models import UserChat
from rest_framework import serializers
from msauthentication.serializers import CustomUserSerializerBaseProfile
from msauthentication.models import CustomUser
from .MessageSerializer import MessageSerializerLastMessage
from mschatroom.models import Message


class UserChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserChat
        fields = "__all__"


class UserChatCustomUserMessageSerializer(serializers.ModelSerializer):
    user = CustomUserSerializerBaseProfile(source="id_user", read_only=True)
    message = MessageSerializerLastMessage(source="return_last_message", read_only=True)

    class Meta:
        model = UserChat
        fields = ["id", "user", "message"]
