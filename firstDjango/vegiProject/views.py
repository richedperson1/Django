from django.shortcuts import render
from .models import *
# Create your views here.

def renderVegi(request):
    if request.method=="POST":
        vegiUploadData = request.POST

        dishNames   = vegiUploadData.get("dish-name")
        dishReceipe = vegiUploadData.get("dish-receipe")
        dishImage   = request.FILES.get("dish-image")

        receipe.objects.create(
            dishName = dishNames,
            dishReceipe = dishReceipe ,
            dishImg = dishImage
        )
    return render(request,"vegiIndex.html")