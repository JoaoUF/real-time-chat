from mschatroom.models import Chat
from mschatroom.serializers import ChatSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView


class ChatList(ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class ChatDetail(RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
