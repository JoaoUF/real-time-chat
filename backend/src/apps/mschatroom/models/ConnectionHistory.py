from django.db import models
from utils.model import Model
from django_extensions.db.models import TimeStampedModel
from msauthentication.models import CustomUser


class ConnectionHistory(Model, TimeStampedModel):
    ONLINE = "online"
    OFFLINE = "offline"
    AWAY = "away"
    STATUS = (
        (ONLINE, "On-line"),
        (OFFLINE, "Off-line"),
        (AWAY, "Away"),
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, db_column="user")
    status = models.CharField(
        max_length=10, choices=STATUS, default=ONLINE, db_column="status"
    )

    class Meta:
        db_table = "MAE_CONNECTION_HISTORY"
