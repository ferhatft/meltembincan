from django.urls import path

from .views import school_sports,soccer_sports,college_programmes,disability,sports_tours,usa_soccer

urlpatterns = [
    path('school-sports/', school_sports, name="school_sports"),
    path('soccer_sports/', soccer_sports, name="school_ssoccer_sportsports"),
    path('college_programmes/', college_programmes, name="college_programmes"),
    path('disability/', disability, name="disability"),
    path('sports_tours/', sports_tours, name="sports_tours"),
    path('usa_soccer/', usa_soccer, name="usa_soccer"),
    
    

]