from django.shortcuts import render
from marketing.models import Signup
from travelblog.models import Blog
# Create your views here.





def home(request):
    featured_blog = Blog.objects.filter(featuredpost=True)
    if request.method=="POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()
    context = {'featured_blog':featured_blog}

    return render(request, 'travel/home.html', context )


def travelInfo(request):
    return render(request, 'travel/travelinfo.html' )


def visaInfo(request):
    return render(request, 'travel/visainfo.html' )

def jobInfo(request):
    return render(request, 'travel/jobinfo.html' )