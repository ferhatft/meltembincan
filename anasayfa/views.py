from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import check_for_language
from django.views.decorators.csrf import csrf_exempt
from haber.models import BlogModel
from kurumsal.models import Client, Team
from portfolio.models import ToursModel


def anasayfa(request):
    team = Team.objects.all()
    tours = ToursModel.objects.all()
    
    bloglast = BlogModel.objects.last()
    blogall = BlogModel.objects.all().exclude(id=bloglast.id)[1:]
    clients = Client.objects.all() 
    
    context = {
        'team':team,
        'tours':tours,
        'bloglast':bloglast,
        'blogall':blogall,
        'clients':clients,
    }
    return render(request, "index.html", context)




def vision(request):
    context = {
    }
    return render(request, "vision.html", context)




