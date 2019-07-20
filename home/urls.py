from django.urls import path
from django.conf.urls import url
from home import views
urlpatterns = [
    path('', views.index, name='index'),
    path('article/<id>/', views.openArticle, name='article'),
    path('news/', views.news),
    path('feedback/', views.feedback),
    path('events/', views.events),
    path('advertise/', views.advertise),
    path('project1/', views.project1),
    path('project2/', views.project2),
    path('project3/', views.project3),
]