from django.shortcuts import render
# Create your views here.

from .models import Team
def hakkimizda(request):
    team = Team.objects.all()
    context = {
        'team' :team, 
    }
    return render(request, "hakkimizda.html", context)

