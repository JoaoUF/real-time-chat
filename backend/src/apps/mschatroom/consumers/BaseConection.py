from channels.generic.websocket import AsyncConsumer
from django.core.exceptions import ObjectDoesNotExist
from channels.db import database_sync_to_async
from mschatroom.models import ConnectionHistory


class BaseConection(AsyncConsumer):

    async def websocket_connect(self, event):
        print("base-connection-stablish")
        user = self.scope["user"]
        self.update_user_status(user, "online")  # type: ignore

    async def websocket_disconnect(self, event):
        print("base-connection-finished")
        user = self.scope["user"]
        self.update_user_status(user, "offline")  # type: ignore

    @database_sync_to_async
    def update_user_status(self, user, status):
        try:
            connection = ConnectionHistory.objects.get(user=user)
            connection.status = status
            return connection.save()
        except ObjectDoesNotExist:
            return ConnectionHistory(user=user).save()
