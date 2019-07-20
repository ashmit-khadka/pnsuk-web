from django.db import models

# Create your models here.
class Member(models.Model):
    forename = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    img = models.CharField(max_length=500, default='https://image.flaticon.com/icons/svg/149/149071.svg')

class Trustee(models.Model):
    forename = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    conact_tel = models.CharField(max_length=50)
    img = models.CharField(max_length=500, default='https://image.flaticon.com/icons/svg/149/149071.svg')

