from django.shortcuts import render
from .models import My_travels_plan, Places_visited, Trip_Details


def index(request):
    
    trips = My_travels_plan.objects.all()
    context = {"trips": trips}
    return render(request, "my_trip_stories/index.html", context)