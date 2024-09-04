from django.db import models
from utils.model import Model
from django_extensions.db.models import TimeStampedModel


class Group(TimeStampedModel, Model):
    name = models.CharField(db_column="name", max_length=100)
    image = models.ImageField(upload_to="group/%Y/%m/%d/")

    class Meta:
        db_table = "MAE_GROUP"
