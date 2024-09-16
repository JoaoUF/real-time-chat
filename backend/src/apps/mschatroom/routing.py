from django.urls import path
from mschatroom.consumers import BaseConection

websocket_urlpatterns = [
    path("chat/<int:user>/", BaseConection.as_asgi()),
]
