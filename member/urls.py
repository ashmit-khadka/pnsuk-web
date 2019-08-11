from django.urls import path
from django.conf.urls import url
from member import views

urlpatterns = [
    path('trustees/', views.trustees),
    path('managment/', views.managment),
    path('advisors/', views.advisors),
    path('membership/', views.membership)
]