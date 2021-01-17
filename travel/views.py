from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'travel/home.html' )


def travelInfo(request):
    return render(request, 'travel/travelinfo.html' )


def visaInfo(request):
    return render(request, 'travel/visainfo.html' )

def jobInfo(request):
    return render(request, 'travel/jobinfo.html' )