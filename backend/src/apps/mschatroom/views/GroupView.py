from mschatroom.models import Group
from mschatroom.serializers import GroupSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView


class GroupList(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupDetail(RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
