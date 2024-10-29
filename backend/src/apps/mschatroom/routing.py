from django.urls import path, re_path
from mschatroom.consumers import CustomUserConsumer

websocket_urlpatterns = [
    re_path(r"ws/chat/$", CustomUserConsumer.as_asgi()),
]
