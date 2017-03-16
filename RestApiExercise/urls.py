"""RestApiExercise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
"""
from django.conf.urls import url
from django.contrib import admin

from restapiapp.views import movie_list, movie_detail

urlpatterns = [

    url(r'^movies/?$', movie_list),
    url(r'^movies/([0-9]+)/?$', movie_detail),
    url(r'^admin/', admin.site.urls),
]
