from django.db import models
from utils.model import Model
from msauthentication.models import CustomUser
from .Chat import Chat
from .Message import Message
from django.db.models import Q


class UserChat(Model):
    id_user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, db_column="id_user"
    )
    id_chat = models.ForeignKey(Chat, on_delete=models.CASCADE, db_column="id_chat")

    class Meta:
        db_table = "MAE_USER_CHAT"

    @property
    def other_user_object(self):
        return CustomUser.objects.get(
            Q(id_chat=self.id_chat) & ~Q(id_user=self.id_user)
        )

    @property
    def return_list_user_chat_related(self):
        return UserChat.objects.filter(
            ~Q(id_user=self.id_user)
            & Q(
                id_chat__in=UserChat.objects.filter(id_user=self.id_user).values(
                    "id_chat"
                )
            )
        )

    @property
    def return_custom_user(self):
        return CustomUser.objects.get(pk=self.id_user)

    @property
    def return_last_message(self):
        return Message.objects.filter(id_chat=self.id_chat).first()
