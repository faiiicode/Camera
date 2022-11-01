from django.contrib import admin
from django.urls import path, include
from . import  views
app_name='cameraapp'
urlpatterns = [
    path('',views.view,name='view'),
    path('registration', views.registration, name='registration'),
    path('subscribe', views.subscribe, name='subscribe')

]

