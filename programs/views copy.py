from django.shortcuts import render,redirect,reverse

from django.db.models import Q

from .models import PortfolioModel,Projelerimiz
# Create your views here.


def portfolio(request):
    products = PortfolioModel.objects.all()
    pagetitle = "ÜRÜNLERİMİZ"
    context = {
        'products':products,
        'pagetitle':pagetitle,
    }
    return render(request, "portfolio.html", context)


def portfoliodetail(request,slug): 
    product = PortfolioModel.objects.get(slug=slug)
    pagetitle = product.title
    context = {
        'product':product,
        'pagetitle':pagetitle,

    }
    return render(request, "portfolio_detail.html", context)




def projelerimiz(request):
    projelerimiz = Projelerimiz.objects.all().order_by('-id')
    pagetitle = 'REFERANS PROJELERİMİZ'
    context = {
        'projelerimiz':projelerimiz,
        'pagetitle':pagetitle,
    }
    return render(request, "projelerimiz.html", context)

