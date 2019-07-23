from django.shortcuts import render
from home.models import *
from advert.models import Advert

# Create your views here.
def index(request):
    articles = Article.objects.all()
    advert = Advert.objects.all()
    context = {
        'articles' : articles,
        'advert' : advert
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
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'home/news.html', context)

def feedback(request):
    
    return render(request, 'home/feedback.html')

def events(request):
    events = Event.objects.all()
    context = {
        'events' : events
    }
    return render(request, 'home/events.html', context)

def advertise(request):
    
    return render(request, 'home/advertise.html')


def project1(request):
    
    return render(request, 'home/project.1.html')
def project2(request):
    
    return render(request, 'home/project.2.html')
def project3(request):
    
    return render(request, 'home/project.3.html')