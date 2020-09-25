from django.urls import path,re_path
from TechTrack.app.views import main_view

urlpatterns = [
    path('',main_view.login,name='login'),
    path('homepage/',main_view.homepage,'homepage'),
    path('logout/',main_view.logout,name='logout_user'),
]
