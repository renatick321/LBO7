from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'bot'

urlpatterns = [
	path('', views.index, name='index'),
]