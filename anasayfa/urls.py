from django.urls import include, path

from .views import anasayfa,vision

urlpatterns = [
    path('', anasayfa, name="anasayfa"),
    path('vision-mission', vision, name="vision"),
    
]