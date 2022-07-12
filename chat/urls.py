from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('<str:R>/', views.Room, name = 'Room'),
    path('checkview', views.checkview, name = 'checkview'),
    path('send', views.send, name = 'send'),
    path('getmessages/<str:R>/', views.getmessages, name = 'getmessages'),
]
