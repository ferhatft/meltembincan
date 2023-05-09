from django.urls import path

from .views import services,servicesdetail 


urlpatterns = [
    path('', services, name="services"),
    path('<slug:slug>', servicesdetail, name="servicesdetail"),

]