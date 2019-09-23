from django.db import models

# Create your models here.
class Advert(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    url = models.CharField(max_length=500, default="test")
    picture = models.ImageField(upload_to='advert_imgs', blank=False, default='default/default.jfif')
    