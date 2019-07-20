from django.contrib import admin
from django.contrib.auth.models import Group

from django.urls import path
from . import views

# Register your models here.
from .models import Article

class articleAdmin(admin.ModelAdmin):
    #change_list_template = 'admin/alter_main.html'
    add_form_template = 'home/newArticle.html'

admin.site.register(Article)