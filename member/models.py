from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    phone = models.CharField(max_length=11, default='0')
    img = models.CharField(max_length=500, default='https://image.flaticon.com/icons/svg/149/149071.svg')

class Trustee(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    phone = models.CharField(max_length=11, default='0')
    email = models.CharField(max_length=100, default='@')
    img = models.CharField(max_length=500, default='https://image.flaticon.com/icons/svg/149/149071.svg')


class Advisor(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=500, default='https://image.flaticon.com/icons/svg/149/149071.svg')
