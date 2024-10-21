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
)
from djangochannelsrestframework.observer import model_observer
from djangochannelsrestframework.decorators import action


class CustomUserConsumer(GenericAsyncAPIConsumer):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializerBaseProfile

    @action()
    async def subscribe_to_connection_history(self, id, request_id, **kwargs):
        self.user_id = id
        await self.connection_history_activity.subscribe(request_id=request_id)  # type: ignore

    @action()
    async def change_connection_history_online(self, **kwargs):
        await self.change_user_connection_status(new_status="online")
        await self.notify_change_user_connection_history()

    @action()
    async def change_connection_history_offline(self, **kwargs):
        await self.change_user_connection_status(new_status="offline")
        await self.notify_change_user_connection_history()

    @action()
    async def list_user_chat(self, **kwarg):
        await self.get_list_user_detail()

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

    async def get_list_user_detail(self):
        listUserChat = await self.get_filter_list_user_chat(self.user_id)
        await self.send_json(
            {
                "type": "list_chat_users",
                "data": [
                    {
                        "uuid_user_chat": userChat.id,
                        "user": {
                            **CustomUserSerializerBaseProfile(
                                await self.get_custom_user(userChat.id_user)
                            ).data  # type: ignore
                        },
                        "message": await {
                            **MessageSerializerLastMessage(
                                await self.get_last_message(userChat.id_chat)
                            ).data  # type: ignore
                        },
                    }
                    for userChat in listUserChat
                ],
            }
        )

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
    def get_last_message(self, uuid_chat):
        return Message.objects.filter(id_chat=uuid_chat).first()

    @database_sync_to_async
    def change_user_connection_status(self, new_status):
        try:
            current_user = CustomUser.objects.get(id=self.user_id)
        except ObjectDoesNotExist:
            raise

        current_history, create = ConnectionHistory.objects.get_or_create(
            user=current_user
        )
        if not create:
            current_history.status = new_status
            current_history.save()


"""
REFERENCES:
- https://djangochannelsrestframework.readthedocs.io/en/latest/examples/filtered_model_observer.html
- https://djangochannelsrestframework.readthedocs.io/en/latest/observer/observer.html#djangochannelsrestframework.observer.model_observer
- https://stackoverflow.com/questions/73952014/subscribe-to-all-changes-of-instances-of-the-model
- https://stackoverflow.com/questions/66166142/contacting-another-websocket-server-from-inside-django-channels
"""
