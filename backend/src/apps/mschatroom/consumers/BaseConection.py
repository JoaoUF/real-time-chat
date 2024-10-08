from channels.generic.websocket import AsyncWebsocketConsumer
from django.core.exceptions import ObjectDoesNotExist
from channels.db import database_sync_to_async
from mschatroom.models import ConnectionHistory
from msauthentication.models import CustomUser


class BaseConection(AsyncWebsocketConsumer):

    async def connect(self):
        self.user = self.scope["url_route"]["kwargs"]["user"]
        await self.update_user_status(self.user, "online")
        await self.accept()

    async def disconnect(self, event):
        self.user = self.scope["url_route"]["kwargs"]["user"]
        await self.update_user_status(self.user, "offline")
        await self.close()

    @database_sync_to_async
    def update_user_status(self, user, set_status) -> None:
        try:
            current_user = CustomUser.objects.get(id=user)
        except ObjectDoesNotExist:
            raise

        current_history, create = ConnectionHistory.objects.get_or_create(
            user=current_user
        )
        if not create:
            current_history.status = set_status
            current_history.save()
