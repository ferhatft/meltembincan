from django.urls import path, include
from .views import blog,blogdetay

urlpatterns = [
    path('', blog, name="blogs"),
    path('<slug:slug>/', blogdetay, name="blogdetay"),
    
]
