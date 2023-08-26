from django.shortcuts import render

# Create your views here.

def renderVegi(request):
    return render(request,"vegiIndex.html")