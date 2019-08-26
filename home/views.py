from django.shortcuts import render
from home.models import *
from advert.models import Advert
import random

# Create your views here.
def index(request):
    articles = Article.objects.raw(
        """
        SELECT *
        FROM home_article
        ORDER BY home_article.date DESC
        LIMIT 3
        """
    )
    projects = Project.objects.raw(
        """
        SELECT *
        FROM home_project
        ORDER BY home_project.date DESC
        LIMIT 3
        """
    )
    events = Event.objects.raw(
        """
        SELECT *
        FROM home_event
        WHERE home_event.date > CURRENT_TIMESTAMP
        ORDER BY home_event.date ASC
        LIMIT 3
        """
        ) 
    front_items = []
    front_items.extend(Article.objects.raw(
        """
        SELECT *
        FROM home_article
        WHERE home_article.home = 1
        ORDER BY home_article.DATE DESC
        """
    ))
    front_items.extend(Project.objects.raw(
        """
        SELECT *
        FROM home_project
        WHERE home_project.home = 1
        ORDER BY home_project.DATE DESC
        """
    ))
    event_past = Event_Past.objects.raw(
    """
    SELECT *
    FROM home_event_past    
    ORDER BY home_event_past.date DESC
    LIMIT 1
    """
    )
    print(event_past[0].text)
    context = {
        'front_items' : front_items,
        'articles' : articles,
        'events' : events,
        'projects' : projects,
        'event_past' : event_past[0]
    }
    return render(request, 'home/index.html', context)


def news(request):
    articles = Article.objects.all().order_by('date').reverse()
    context = {
        'articles' : articles,
    }
    return render(request, 'home/news.html', context)

def feedback(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'home/feedback.html', context)
def events_past(request):    
    events = Event.objects.raw(
        """
        SELECT * 
        FROM home_event
        WHERE home_event.date < CURRENT_TIMESTAMP
        ORDER BY home_event.date DESC
        """
        )

    events_past = Event_Past.objects.all()
    
    context = {
        'events' : events,
        'events_past' : events_past,
    }
    return render(request, 'home/events_past.html', context)


def events(request):    
    events = Event.objects.raw(
        """
        SELECT * 
        FROM home_event
        WHERE home_event.date > CURRENT_TIMESTAMP
        ORDER BY home_event.date ASC
        """
        ) 
    context = {
        'events' : events,
    }
    return render(request, 'home/events_upcoming.html', context)

def advertise(request):
    return render(request, 'home/advertise.html')

def guests(request):
    guests = Guest.objects.all()

    context = {
        'guests' : guests
    }
    return render(request, 'home/guests.html', context)
    

def openArticle(request, id):
    article = Article.objects.get(id=id)
    articles = Article.objects.raw(
        """
        SELECT *
        FROM home_article
        ORDER BY home_article.date DESC
        LIMIT 3
        """
    )
    context = {
        'article' : article,
        'articles' : articles
    }
    return render(request, 'home/article.html', context)


def openEvent(request, id):
    event = Event_Past.objects.get(id=id)
    context = {
        'event' : event
    }
    return render(request, 'home/event.html', context)


def openProject(request, id):
    project = Project.objects.get(id=id)
    context = {
        'project' : project
    }
    return render(request, 'home/project.html', context)