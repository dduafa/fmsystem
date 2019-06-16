from django.shortcuts import render
from django.http import HttpRequest

def create_station_view(request): 
    assert isinstance(request, HttpRequest)   
    return render(request, "create_station.html")
