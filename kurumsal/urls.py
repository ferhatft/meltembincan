from django.urls import path

from .views import hakkimizda


urlpatterns = [
    path('about-us', hakkimizda, name="hakkimizda"),
]