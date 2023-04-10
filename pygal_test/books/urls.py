from django.contrib import admin
from django.urls import path 
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path(route='', view=views.BookGraph, name='BookGraph')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)