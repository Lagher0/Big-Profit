from django.http import HttpResponse
from django.shortcuts import render
from hunt import hunt

def index(request):
    return render(request, 'index.html')

def startadventure(request):
    if request.method == 'POST':
        time_constraint = float(request.POST['time_option'])
        place_category = request.POST.getlist('category')
        radius = float(request.POST['distance_option'])
        dahunt = hunt(time_constraint,radius)
        return render(request,'startadventure.html',{"time_option":time_constraint, "category":place_category, "distance_option":radius,"dahunt":dahunt})
