from django.shortcuts import render



def blogView(request):

    return render(request, 'travelblog/blogview.html')



def blogDetail(request):
    return render(request, 'travelblog/blogdetails.html')