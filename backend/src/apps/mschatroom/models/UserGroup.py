from django.db import models
from utils.model import Model
from msauthentication.models import CustomUser
from .Group import Group


class UserGroup(Model):
    id_user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, db_column="id_user"
    )
    id_group = models.ForeignKey(Group, on_delete=models.CASCADE, db_column="id_group")

    class Meta:
        db_table = "MAE_USER_GROUP"
