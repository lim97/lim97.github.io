from django.utils import timezone

from django.db import models
from home import  models as home_models


class News(home_models.TimeStampedModel):
        date = models.DateField(default=timezone.now)
        name = models.CharField(max_length=80,default=True)

        description = models.TextField(default=True)
        class Meta:
                verbose_name = "New"

