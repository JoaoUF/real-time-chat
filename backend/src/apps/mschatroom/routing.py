from django.urls import path
from .consumers import MyConsumer

websocket_urlpatterns = [
    path("chat/", MyConsumer.as_asgi()),
]
