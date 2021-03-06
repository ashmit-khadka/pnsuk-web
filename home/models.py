from django.db import models
from django.core.validators import MaxLengthValidator

class Event(models.Model):
    name = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    date = models.DateTimeField() 
    contact = models.CharField(max_length=100)
    other = models.CharField(max_length=2000)

class Policy(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField()
 
class Project(models.Model):
    title = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='project_imgs', blank=False, default='default/default.jfif')
    date = models.DateField() 
    text = models.CharField(max_length=10000)
    home = models.BooleanField(default=False)
    news = models.BooleanField(default=False)

class Event_Past(models.Model):
    title = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='event_imgs', blank=False, default='default/default.jfif')
    date = models.DateField() 
    text = models.CharField(max_length=10000)
    home = models.BooleanField(default=False)
    news = models.BooleanField(default=False)
    aid = models.BooleanField(default=False)

class Guest(models.Model):
    title = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='guestt_imgs', blank=False, default='default/default.jfif')
    date = models.DateField() 
    text = models.CharField(max_length=10000)
    home = models.BooleanField(default=False)
    news = models.BooleanField(default=False)

class Minutes(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField()


