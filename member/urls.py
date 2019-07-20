from django.urls import path
from django.conf.urls import url
from member import views

urlpatterns = [
    path('', views.index, name='index'),
    path('committee/', views.committee),
    path('advisory/', views.advisory)

]