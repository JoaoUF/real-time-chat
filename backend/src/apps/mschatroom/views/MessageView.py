from mschatroom.models import Message
from mschatroom.serializers import MessageSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView


class MessageList(ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageDetail(RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
