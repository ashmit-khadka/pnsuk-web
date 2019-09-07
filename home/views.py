from django.shortcuts import render
from home.models import *
from advert.models import Advert
import random
import smtplib

# Create your views here.
def index(request):
    projects = Project.objects.raw(
        """
        SELECT *
        FROM home_project
        ORDER BY home_project.date DESC
        LIMIT 2
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

    front_items = getLatest()

    event_past = Event_Past.objects.raw(
        """
        SELECT *
        FROM home_event_past    
        ORDER BY home_event_past.date DESC
        LIMIT 2
        """
    )
    guests = Guest.objects.raw(
        """
        SELECT *
        FROM home_guest    
        ORDER BY home_guest.date DESC
        LIMIT 2
        """
    )
    context = {
        'front_items' : front_items,
        'events' : events,
        'projects' : projects,
        'event_past' : event_past,
        'guests' : guests
    }
    return render(request, 'home/index.html', context)


def news(request):
    articles = []
    articles.extend(Event_Past.objects.raw(
        """
        SELECT
        *,
        'event' AS Type
        FROM home_event_past
        WHERE home_event_past.news = 1
        """
    ))
    articles.extend(Project.objects.raw(
        """
        SELECT
        *,
        'project' AS Type
        FROM home_project
        WHERE home_project.news = 1
        """
    ))
    articles.extend(Guest.objects.raw(
        """
        SELECT
        *,
        'guest' AS Type
        FROM home_guest
        WHERE home_guest.news = 1
        """
    ))
    articles.sort(key=lambda x: x.date, reverse=True)
    context = {
        'articles' : articles,
    }
    return render(request, 'home/news.html', context)

def feedback(request):
    return render(request, 'home/feedback.html')


def events_past(request):    

    events_past = Event_Past.objects.raw(
        """
        SELECT * 
        FROM home_event_past
        ORDER BY home_event_past.date DESC
        """
    ) 

    context = {
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
    guests = Guest.objects.raw(
        """
        SELECT * 
        FROM home_guest
        ORDER BY home_guest.date DESC
        """
        )
    context = {
        'guests' : guests
    }
    return render(request, 'home/guests.html', context)

def openEvent(request, id):
    event = Event_Past.objects.get(id=id)
    latestItems = getLatest()

    context = {
        'article' : event,
        'latestItems' : latestItems
    }
    return render(request, 'home/article.html', context)


def openProject(request, id):
    project = Project.objects.get(id=id)
    latestItems = getLatest()
    context = {
        'article' : project,
        'latestItems' : latestItems
    }
    return render(request, 'home/article.html', context)


def openGuest(request, id):
    guest = Guest.objects.get(id=id)
    latestItems = getLatest()
    context = {
        'article' : guest,
        'latestItems' : latestItems
    }
    return render(request, 'home/article.html', context)

def sendFeedback(request):
    response = 0
    if request.method == 'POST':
        print(request.POST.get('title'))
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        body = "Name: %s\nEmail: %s\nMessage: %s\n" % (name, email, message)
        response == send_email(subject, body, email)

    return feedback(request)

def send_email(subject, msg, email):
    try:
        server = smtplib.SMTP('smtp-mail.outlook.com:587')
        server.ehlo()
        server.starttls()
        server.login('pnsuk.org.es@outlook.com', 'Society@7')
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail('pnsuk.org.es@outlook.com', 'pnsuk.org@hotmail.com', message)
        server.sendmail('pnsuk.org.es@outlook.com', email, 'Your message to PNS has been sent, Thank you for your feedback.')

        server.quit()
        print("Success: Email sent!")
        return 1
    except:
        print("Email failed to send.")
        return 0

def getLatest():
    front_items = []
    
    front_items.extend(Event_Past.objects.raw(
        """
        SELECT
        *,
        'event' AS Type
        FROM home_event_past
        WHERE home_event_past.home = 1
        ORDER BY home_event_past.DATE DESC
        """
    ))

    front_items.extend(Guest.objects.raw(
        """
        SELECT
        *,
        'guest' AS Type
        FROM home_guest
        WHERE home_guest.home = 1
        ORDER BY home_guest.DATE DESC
        """
    ))
    front_items.extend(Project.objects.raw(
        """
        SELECT
        *,
        'project' AS Type
        FROM home_project
        WHERE home_project.home = 1
        ORDER BY home_project.DATE DESC
        """
    ))

    return front_items