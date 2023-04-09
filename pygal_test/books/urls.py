from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path(route='', view=views.BookGraph, name='BookGraph')
]