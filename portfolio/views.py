from django.shortcuts import render,redirect

from django.db.models import Q

from .models import Category,ToursModel

# Create your views here.


def services(request):
    pagetitle = "ÜRÜNLERİMİZ"
    category = Category.objects.all()
    context = {
        'pagetitle':pagetitle,
        'category':category,
    }
    return render(request, "portfolio.html", context)


def servicesdetail(request,slug): 
    tours = ToursModel.objects.get(slug=slug)
    pagetitle = tours.title
    context = {
        'tours':tours,
        'pagetitle':pagetitle,

    }
    return render(request, "tours_detail.html", context)
