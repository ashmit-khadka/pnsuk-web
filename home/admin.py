from django.contrib import admin
# Register your models here.
from .models import Article
from .models import Event
from .models import Policy
from .models import Project
from .models import Event_Past
from .models import Guest
from django import forms
 
 
class ArticleModelForm( forms.ModelForm ):
    text = forms.CharField( widget=forms.Textarea )
    class Meta:
        model = Article
        fields = '__all__'  

class ArticleAdmin( admin.ModelAdmin ):
    form = ArticleModelForm
    list_display = (
        'title',
        'date',
        'home',
        )

class EventModelForm( forms.ModelForm ):
    other = forms.CharField( widget=forms.Textarea )
    class Meta:
        model = Event
        fields = '__all__'        
 
class EventAdmin( admin.ModelAdmin ):
    form = EventModelForm
    list_display = (
        'name',
        'date',
        'venue',
        )

class ProjectModelForm( forms.ModelForm ):
    text = forms.CharField( widget=forms.Textarea )
    class Meta:
        model = Project
        fields = '__all__'  

class ProjectAdmin( admin.ModelAdmin ):
    form = ProjectModelForm
    list_display = (
        'title',
        'date',
        'home',
        )  

class PolicyAdmin( admin.ModelAdmin ):
    list_display = (
        'name',
        )
class Event_PastModelForm( forms.ModelForm ):
    text = forms.CharField( widget=forms.Textarea )
    class Meta:
        model = Event_Past
        fields = '__all__'  

class Event_PastAdmin( admin.ModelAdmin ):
    form = Event_PastModelForm
    list_display = (
        'title',
        'date',
        'home',
        )

class GuestModelForm( forms.ModelForm ):
    text = forms.CharField( widget=forms.Textarea )
    class Meta:
        model = Guest
        fields = '__all__'  

class GuestAdmin( admin.ModelAdmin ):
    form = GuestModelForm
    list_display = (
        'title',
        'date',
        'home',
        )

    

admin.site.register(Article, ArticleAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Policy, PolicyAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Event_Past, Event_PastAdmin)
admin.site.register(Guest, GuestAdmin)

