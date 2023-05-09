from django.urls import include, path
from .views import (
    contacview,newsletterview
)

urlpatterns = [
    path('' , contacview, name="iletisim"),   
    path('add/' , newsletterview, name="newsletterview"),
]

