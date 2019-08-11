from django.contrib import admin
# Register your models here.
from .models import Article
from .models import Event
from .models import Policy
from django import forms
 
 
class ArticleModelForm( forms.ModelForm ):
    text = forms.CharField( widget=forms.Textarea )
    class Meta:
        model = Article
        fields = '__all__'        

    list_display = (
        'title',
        )  
 
class ArticleAdmin( admin.ModelAdmin ):
    form = ArticleModelForm

class EventModelForm( forms.ModelForm ):
    other = forms.CharField( widget=forms.Textarea )
    class Meta:
        model = Event
        fields = '__all__'
        
 
class EventAdmin( admin.ModelAdmin ):
    form = EventModelForm



admin.site.register(Article, ArticleAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Policy)

