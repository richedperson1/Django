from django.urls import path
from . import views
from django.http import HttpResponse

def dynamicURL(request,age):
    return HttpResponse(f"The age of student is {age}")

def dynamicURL2(request,name):
    return HttpResponse(f"The name of student is {name}")

urlpatterns = [
    path("/<int:age>",dynamicURL),
    path("/",views.aboutPage),
    path("/details",views.rendingDataAbout)
]


