from django.db import models
from home import  models as home_models


class Question(home_models.TimeStampedModel):
    name = models.CharField(max_length=80, default=True ,null=True)
    date = models.CharField(max_length=80, default=True,null=True)
    def __str__(self):
        return self.name


