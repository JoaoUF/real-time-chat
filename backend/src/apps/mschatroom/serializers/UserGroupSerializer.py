from mschatroom.models import UserGroup
from rest_framework import serializers


class UserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroup
        fields = "__all__"
