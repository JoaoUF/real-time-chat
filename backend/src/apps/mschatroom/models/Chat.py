from utils.model import Model
from django_extensions.db.models import TimeStampedModel


class Chat(TimeStampedModel, Model):
    class Meta:
        db_table = "MAE_CHAT"
