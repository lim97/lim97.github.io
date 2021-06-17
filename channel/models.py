from abc import abstractproperty

from django.db import models
from home import  models as home_models


class AbstractItem(home_models.TimeStampedModel):
        name = models.CharField(max_length=80)
        class Meta:
                 abstract = True
        def __str__(self):
                 return self.name

class ChannelType(AbstractItem):
        class Meta:
                verbose_name ="Channel Type"


class ChannelImg(home_models.TimeStampedModel):
        name = models.CharField(max_length=80,null=True)
        file = models.ImageField(upload_to="ch_photos",null=True)
        channel = models.ForeignKey("Channel",related_name="chimg",on_delete=models.CASCADE,null=True)
        def __str__(self):
                return self.name

class Channel(home_models.TimeStampedModel):
        name = models.CharField(max_length=140, default=True)
        link = models.CharField(max_length=140, default=True)
        description = models.CharField(max_length=140, default=True)
        channeltype = models.ForeignKey(ChannelType,related_name="channeltype",on_delete=models.SET_NULL,null=True,default=True)



        def __str__(self):
                return self.name

        def ch_img(self):
                img, = self.chimg.all()

                return img.file.url







