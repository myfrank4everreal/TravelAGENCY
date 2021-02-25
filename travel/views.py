from jobs.models import JobAdmin, JobPost
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect, render
from marketing.models import Signup
from travelblog.models import Blog
from jobs.models import JobPost



from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.





def home(request):
    featured_blog = Blog.objects.filter(featuredpost=True)
    most_recent_jobs = JobPost.objects.order_by("-post_date")[0:4]
    if request.method=="POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()
    context = {
        'featured_blog':featured_blog,
        'most_recent_jobs':most_recent_jobs,
        
    }

    return render(request, 'travel/home.html', context )

def aboutUs(request):
    
    return render(request, 'travel/aboutus.html')


@login_required
def dashBoard(response):

    # all_user_post = JobPost.objects.filter(related_name="job_admin_name")
    # # all_user_post = JobAdmin(response.user)


    # if all_user_post in response.user.job_admin_name.all():
    #     print(all_user_post)
        
    
    # else:
    #     print('no users found by my findin frank')    

    
            
    
        # return render(response, 'travel/dashboard.html', {'all_user_post':all_user_post})
    return render(response, 'travel/dashboardactive.html')


def travelInfo(request):
    return render(request, 'travel/travelinfo.html' )


def visaInfo(request):
    return render(request, 'travel/visainfo.html' )






