from django.urls import path
from django.conf.urls import url
from home import views
urlpatterns = [
    path('', views.index, name='index'),
    path('news/', views.news),
    path('feedback/', views.feedback),
    path('events/', views.events),
    path('events-past/', views.events_past),
    path('advertise/', views.advertise),
    path('project/<id>/', views.openProject),
    path('event/<id>/', views.openEvent),
    path('guest/<id>/', views.openGuest),   
    path('guests/', views.guests),    
    path('sendFeedback/', views.sendFeedback),
    path('aid/', views.aid),   
    path('minutes/', views.minutes)
]