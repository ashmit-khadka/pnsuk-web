from django.db import models
from django.core.validators import MaxLengthValidator

class Article(models.Model):
    title = models.CharField(max_length=50)
    image = models.CharField(max_length=50, default="def.png")
    date = models.DateField() 
    text = models.CharField(max_length=10000)
 