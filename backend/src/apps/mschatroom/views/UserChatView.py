from mschatroom.models import UserChat
from mschatroom.serializers import UserChatSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView


class UserChatList(ListCreateAPIView):
    queryset = UserChat.objects.all()
    serializer_class = UserChatSerializer


class UserChatDetail(RetrieveUpdateDestroyAPIView):
    queryset = UserChat.objects.all()
    serializer_class = UserChatSerializer
