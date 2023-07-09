from django.urls import path
from . import views
from django.http import HttpResponse

"""

The function takes a request and an age as parameters and returns a response with the age of the
student.

:param request: The request parameter is an object that represents the HTTP request made by the
client. It contains information such as the HTTP method, headers, and body of the request
:param age: The age parameter is the age of the student. It is passed as an argument to the
dynamicURL function
:return: an HttpResponse object that contains a string message. The message includes the age of the
student.

"""
def dynamicURL(request,age):
    
    return HttpResponse(f"The age of student is {age}")

def dynamicURL2(request,name):
    return HttpResponse(f"The name of student is {name}")

urlpatterns = [
    path("<int:age>",dynamicURL),
    path("",views.aboutPage),
    path("details",views.rendingDataAbout)
]


