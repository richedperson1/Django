from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def aboutPage(request):
    return HttpResponse("This is the About page of the Django APP")


def rendingDataAbout(request):
    peopleData = [
        {"name":"Rutvik",
         "LastName":"Jaiswal",
         "RollNum":29,
         "CompanyName":"Amazon"
         },
        {"name":"Jadu",
         "LastName":"Jaiswal",
         "RollNum":28,
         "CompanyName":"Harman"
         },
        {"name":"Prasad",
         "LastName":"Jaiswal",
         "RollNum":26,
         "CompanyName":"Microsoft"
         }
    ]

    return render(request,"aboutPage.html",context={"peopleData":peopleData})