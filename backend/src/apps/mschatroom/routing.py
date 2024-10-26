from django.urls import path, re_path
from mschatroom.consumers import CustomUserConsumer

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<id>\w+)/$", CustomUserConsumer.as_asgi()),
]
