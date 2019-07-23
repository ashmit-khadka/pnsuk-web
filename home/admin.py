from django.contrib import admin
from django.contrib.auth.models import Group
from django.urls import path
from . import views
from django.forms import TextInput, Textarea
from django.db import models


# Register your models here.
from .models import Article
from .models import Event

class articleAdmin(admin.ModelAdmin):
    #change_list_template = 'admin/alter_main.html'
    add_form_template = 'home/newArticle.html'

class YourModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }


admin.site.register(Article)
admin.site.register(Event, YourModelAdmin)
