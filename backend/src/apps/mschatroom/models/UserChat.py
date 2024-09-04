from django.db import models
from utils.model import Model
from msauthentication.models import CustomUser
from .Chat import Chat


class UserChat(Model):
    id_user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, db_column="id_user"
    )
    id_chat = models.ForeignKey(Chat, on_delete=models.CASCADE, db_column="id_chat")

    class Meta:
        db_table = "MAE_USER_CHAT"
