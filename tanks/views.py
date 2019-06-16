from django.shortcuts import render
from django.http import HttpRequest

def create_tank_view(request): 
    assert isinstance(request, HttpRequest)   
    return render(request, "create_tank.html")

def signup(request):
    assert isinstance(request, HttpRequest)
    return render(request, "signup.html", {})