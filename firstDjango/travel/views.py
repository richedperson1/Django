from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def travelHello(request):
    return render(request,"travel.html")

# Create your views here.

def travelHello2(request):
    return HttpResponse("This is for nested routing which is first main urls then apps urls")