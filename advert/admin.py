from django.contrib import admin
from .models import Advert


# Register your models here.


class AdvertAdmin( admin.ModelAdmin ):
    list_display = (
        'name',        
        )

admin.site.register(Advert, AdvertAdmin)