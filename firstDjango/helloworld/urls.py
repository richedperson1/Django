from django.urls import path

from . import views

urlpatterns = [
    path("",views.helloWorld),
    path("data",views.helloWorldData)
]