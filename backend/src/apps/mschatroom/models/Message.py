from django.db import models
from utils.model import Model
from msauthentication.models import CustomUser
from .Group import Group
from .Chat import Chat


class Message(Model):
    id_user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, db_column="id_user"
    )
    id_group = models.ForeignKey(
        Group, on_delete=models.CASCADE, db_column="id_group", null=True, blank=True
    )
    id_chat = models.ForeignKey(
        Chat, on_delete=models.CASCADE, db_column="id_chat", null=True, blank=True
    )
    content = models.TextField(db_column="content")
    sent_at = models.DateField(auto_now=False, auto_now_add=True, db_column="sent_at")
    deliverated = models.BooleanField(db_column="deliverated", default=False)
    seen = models.BooleanField(db_column="seen", default=False)

    class Meta:
        db_table = "MAE_MESSAGE"
        ordering = ["-sent_at"]
