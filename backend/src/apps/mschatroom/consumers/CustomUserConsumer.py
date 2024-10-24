from django.http import JsonResponse
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    DeleteModelMixin,
)
from django.core.exceptions import ObjectDoesNotExist
from channels.db import database_sync_to_async
from mschatroom.models import UserChat, ConnectionHistory, Message
from msauthentication.models import CustomUser
from msauthentication.serializers import CustomUserSerializerBaseProfile
from mschatroom.serializers import (
    MessageSerializerLastMessage,
    ConnectionHistorySerializer,
    UserChatCustomUserMessageSerializer,
)
from djangochannelsrestframework.observer import model_observer
from djangochannelsrestframework.decorators import action


"""
DOTO:
- create a disconnect function which erase user_id and change to offline
"""


class CustomUserConsumer(GenericAsyncAPIConsumer):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializerBaseProfile

    async def disconnect(self, code):
        if hasattr(self, "user_id"):
            await self.change_user_connection_status(new_status="offline")
            await self.notify_change_user_connection_history()
        return await super().disconnect(code)

    @action()
    async def subscribe_to_connection_history(self, id, request_id, **kwargs):
        if await self.check_custom_user_exist(pk=id):
            self.user_id = id
        else:
            raise
        await self.connection_history_activity.subscribe(request_id=request_id)  # type: ignore

    @action()
    async def change_connection_history_online(self, **kwargs):
        await self.change_user_connection_status(new_status="online")
        await self.notify_change_user_connection_history()

    @action()
    async def list_user_chat(self, **kwarg):
        listUserChat = await self.get_filter_list_user_chat(pk=self.user_id)
        await self.send_json(
            {
                "type": "list_chat_users",
                "data": await self.get_user_rooms_data(listUserChat),
            }
        )

    @model_observer(ConnectionHistory)
    async def connection_history_activity(  # type: ignore
        self,
        message,
        observer: None,
        subscribing_request_ids=[],
        **kwargs,
    ):
        pass

    @connection_history_activity.groups_for_consumer  # type: ignore
    def connection_history_activity(self, sesion=None, **kwargs):
        if sesion is not None:
            print(f"-user__{sesion}")
            yield f"-user__{sesion}"

    async def notify_change_user_connection_history(self):
        print("notify other users")
        listIdChat = await self.get_list_id_chat()
        print("mostrar grupos", self.groups)
        for group in self.groups:
            print("group--", group)
            if group[6:] in listIdChat:
                await self.channel_layer.group_send(  # type: ignore
                    group,
                    {
                        "type": "update_connection_history",
                        "user": {
                            **CustomUserSerializerBaseProfile(
                                await self.get_custom_user(int(group[6:]))
                            ).data  # type: ignore
                        },
                    },
                )

    @database_sync_to_async
    def get_user_rooms_data(self, list_user_chat):
        return [
            {**UserChatCustomUserMessageSerializer(userChat).data}  # type: ignore
            for userChat in list_user_chat
        ]

    @database_sync_to_async
    def get_list_id_chat(self):
        return UserChat.objects.filter(id_user=self.user_id).values("id_chat")

    @database_sync_to_async
    def get_filter_list_user_chat(self, pk: int):
        return UserChat.objects.get(id_user=pk).return_list_user_chat_related

    @database_sync_to_async
    def get_custom_user(self, pk: int) -> CustomUser:
        return CustomUser.objects.get(pk=pk)

    @database_sync_to_async
    def check_custom_user_exist(self, pk: int) -> bool:
        return CustomUser.objects.filter(pk=pk).exists()

    @database_sync_to_async
    def change_user_connection_status(self, new_status) -> None:
        try:
            current_user = CustomUser.objects.get(id=self.user_id)
            current_history, create = ConnectionHistory.objects.get_or_create(
                user=current_user
            )
            if not create:
                current_history.status = new_status
                current_history.save()
        except ObjectDoesNotExist:
            raise
