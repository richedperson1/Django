from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def helloWorld(request):
    dist = {"Name":"Rutvik","lName":"Jaiswal"}
    return render(request,"index.html",dist)


def helloWorldData(request):
    return render(request,"data.html")