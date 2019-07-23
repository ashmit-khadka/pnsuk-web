from django.db import models
from django.core.validators import MaxLengthValidator

class Article(models.Model):
    title = models.CharField(max_length=50)
    image = models.CharField(max_length=50, default="def.png")
    date = models.DateField() 
    text = models.CharField(max_length=10000)

class Event(models.Model):
    name = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    date = models.DateTimeField() 
    contact = models.CharField(max_length=100)
    other = models.CharField(max_length=2000)

 