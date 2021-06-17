from django.db import models
from home import  models as home_models




class CalenImg(home_models.TimeStampedModel):
        name = models.CharField(max_length=80,null=True)
        file = models.ImageField(upload_to="ca_photos",null=True)
        calen = models.ForeignKey("Calendars",related_name="caimg",on_delete=models.CASCADE,null=True)
        def __str__(self):
                return self.name


class Calendars(home_models.TimeStampedModel):
        date = models.CharField(max_length=80,default=True)
        name = models.CharField(max_length=80,default=True)
        subname =models.CharField(max_length=200,default=True)
        description = models.TextField(max_length=1000,default=True)

        def __str__(self):
                return self.name
        class Meta:
                verbose_name = "Calendar"

        def ca_img(self):
                img, = self.caimg.all()
                return img.file.url