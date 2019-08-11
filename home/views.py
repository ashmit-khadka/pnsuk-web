from django.shortcuts import render
from home.models import *
from advert.models import Advert
import random

# Create your views here.
def index(request):
    articles = Article.objects.all()
    advert = Advert.objects.all().order_by('?')
    events = Event.objects.all().order_by('date')
    context = {
        'articles' : articles,
        'advert' : advert,
        'events' : events
    }
    return render(request, 'home/index.html', context)

def openArticle(request, id):
    article = Article.objects.get(id=id)
    articles = Article.objects.all()
    context = {
        'article' : article,
        'articles' : articles
    }
    return render(request, 'home/article.html', context)

def news(request):
    advert = Advert.objects.all()
    articles = Article.objects.all()
    context = {
        'articles' : articles,
        'advert' : advert
    }
    return render(request, 'home/news.html', context)

def feedback(request):
    advert = Advert.objects.all().order_by('?')
    articles = Article.objects.all()
    context = {
        'articles' : articles,
        'advert' : advert
    }
    return render(request, 'home/feedback.html', context)

def events(request):    
    advert = Advert.objects.all().order_by('?')
    articles = Article.objects.all()
    events = Event.objects.all().order_by('date')
    context = {
        'events' : events,
        'articles' : articles,
        'advert' : advert
    }
    return render(request, 'home/events.html', context)

def advertise(request):
    advert = Advert.objects.all().order_by('?')
    articles = Article.objects.all()
    context = {
        'articles' : articles,
        'advert' : advert
    }
    return render(request, 'home/advertise.html', context)

def project1(request):    
    return render(request, 'home/project.1.html')
def project2(request):    
    return render(request, 'home/project.2.html')
def project3(request):    
    return render(request, 'home/project.3.html')