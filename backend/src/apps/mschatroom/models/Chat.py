from utils.model import Model
from django_extensions.db.models import TimeStampedModel
from models import UserChat
from msauthentication.models import CustomUser


class Chat(TimeStampedModel, Model):
    class Meta:
        db_table = "MAE_CHAT"

    @property
    def return_user(self):
        userChat = UserChat.objects.get(id=self.id)
        return CustomUser.objects.get(user=userChat)
