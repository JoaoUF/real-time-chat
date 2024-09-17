from mschatroom.models import UserChat
from rest_framework import serializers
from msauthentication.serializers import CustomUserSerializerBaseProfile
from MessageSerializer import MessageSerializerLastMessage


class UserChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserChat
        fields = "__all__"


class UserChatSerializerListStatus(serializers.ModelSerializer):
    user = CustomUserSerializerBaseProfile(source="other_user_object")
    message = MessageSerializerLastMessage(source="get_last_message")

    class Meta:
        model = UserChat
        fields = ["id_chat", "user", "message"]
