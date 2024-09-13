from mschatroom.models import UserChat
from rest_framework import serializers


class UserChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserChat
        fields = "__all__"
