"""Enso TOP-LEVEL URL Configuration
"""
from django.contrib import admin
from django.urls import include,path,re_path

BASE_URL_CONTROLLER_DIR = 'TechTrack.app.controllers.url.'

urlpatterns = [
    path('admin/', admin.site.urls),
    #Main URLS
    path('', include(BASE_URL_CONTROLLER_DIR + 'main_urls')),

]
