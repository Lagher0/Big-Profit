from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def startadventure(request):
    if request.method == 'POST':
        score = 3
        time_constraint = request.POST['time_option']
        place_category = request.POST.getlist('category')
        radius = request.POST['distance_option']
        return render(request,'startadventure.html',{"time_option":time_constraint, "category":place_category, "distance_option":radius,"score":score})
