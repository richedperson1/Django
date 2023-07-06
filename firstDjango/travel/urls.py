from django.urls import path
from django.shortcuts import render

from . import views



urlpatterns = [
    path("",views.travelHello,name="travelWeb"),
    path("change",views.travelHello2,name="travelWeb")
]