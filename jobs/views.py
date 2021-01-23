from django.http import request
from django.shortcuts import render





def jobView(request):
    return render(request, 'jobs/jobview.html')