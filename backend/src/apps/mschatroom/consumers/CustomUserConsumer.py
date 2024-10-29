from django.core.exceptions import ObjectDoesNotExist
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from channels.db import database_sync_to_async
from mschatroom.models import UserChat, ConnectionHistory
from msauthentication.models import CustomUser
from msauthentication.serializers import CustomUserSerializerBaseProfile
from mschatroom.serializers import UserChatCustomUserMessageSerializer
from djangochannelsrestframework.observer import model_observer
from djangochannelsrestframework.decorators import action
from rest_framework import status
from django.http.response import Http404


"""
TODO:
- add a model observer for UserChat
- add a filtered model observer for Messages

CKECK:
- if send to a particular users using a model observer
- if create a filtered model for each user
"""


class CustomUserConsumer(GenericAsyncAPIConsumer):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializerBaseProfile

    @action()
    async def subscribe_history_activity(self, request_id, **kwargs):
        await self.exist_custom_user(pk=request_id)
        await self.connection_history_activity.subscribe(request_id=request_id)  # type: ignore
        return {}, status.HTTP_200_OK

    @action()
    async def unsubscribe_history_activity(self, request_id, **kwargs):
        await self.exist_custom_user(pk=request_id)
        await self.connection_history_activity.unsubscribe(request_id=request_id)  # type: ignore
        return {}, status.HTTP_200_OK

    @action()
    async def patch_user_status(self, request_id, status, **kwargs):
        await self.exist_custom_user(pk=request_id)
        await self.path_user_connection_status(new_status=status, pk=request_id)
        return {}, status.HTTP_200_OK

    @action()
    async def get_list_user_chat(self, request_id, **kwarg):
        await self.exist_custom_user(pk=request_id)
        listUserChat = await self.get_filter_list_user_chat(id=request_id)
        await self.send_json(
            {
                "type": "list_chat_users",
                "data": await self.get_user_rooms_data(listUserChat),
            },
        )

    # print subscribing_requets_ids
    # check if print my request_id
    # check if send other users works adding the the value in a dict
    @model_observer(ConnectionHistory)
    async def connection_history_activity(  # type: ignore
        self, message, observer: None, subscribing_request_ids=[], **kwargs
    ):
        pass
        # print("OBSERVER")
        # print("subscribing-request-list", subscribing_request_ids)
        # print("request_id", request_id)  # type: ignore

    @database_sync_to_async
    def get_user_rooms_data(self, list_user_chat):
        return [
            {**UserChatCustomUserMessageSerializer(userChat).data}  # type: ignore
            for userChat in list_user_chat
        ]

    # @database_sync_to_async
    # def get_list_id_chat(self):
    #     return UserChat.objects.filter(id_user=self.user_id).values("id_chat")

    @database_sync_to_async
    def get_filter_list_user_chat(self, pk: int):
        return UserChat.objects.get(id_user=pk).return_list_user_chat_related

    @database_sync_to_async
    def get_custom_user(self, pk: int) -> CustomUser:
        return CustomUser.objects.get(pk=pk)

    @database_sync_to_async
    def exist_custom_user(self, pk: int):
        if not CustomUser.objects.filter(pk=pk).exists():
            raise Http404

    @database_sync_to_async
    def path_user_connection_status(self, new_status, pk):
        current_user = CustomUser.objects.get(id=pk)
        current_history, create = ConnectionHistory.objects.get_or_create(
            user=current_user
        )
        if not create:
            current_history.status = new_status
            current_history.save()
