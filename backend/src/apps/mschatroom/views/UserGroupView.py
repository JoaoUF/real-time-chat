from mschatroom.models import UserGroup
from mschatroom.serializers import UserGroupSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView


class UserGroupList(ListCreateAPIView):
    queryset = UserGroup.objects.all()
    serializer_class = UserGroupSerializer


class UserGroupDetail(RetrieveUpdateDestroyAPIView):
    queryset = UserGroup.objects.all()
    serializer_class = UserGroupSerializer
