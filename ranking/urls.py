from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('newgame', views.newgame, name='newgame'),
    path('getinf', views.getinf, name='getinf'),
    path('getcsv', views.getcsv, name='getcsv'),
    path('postinf', views.postinf, name='postinf'),
    path('postnewgame', views.postnewgame, name='postnewgame'),
]

