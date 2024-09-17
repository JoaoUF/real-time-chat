from django.urls import path, re_path
from mschatroom.consumers import BaseConection

websocket_urlpatterns = [
    # path("chat/<int:user>/", BaseConection.as_asgi()),
    re_path(r"ws/chat/(?P<user>\w+)/$", BaseConection.as_asgi()),
]
