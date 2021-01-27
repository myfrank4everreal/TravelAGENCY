from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from .models import JobAdmin, JobPost
from .forms import JobListForm
from django.db.models.query import QuerySet
from django.db.models import Q
from django.urls.base import reverse
from django.core.checks import messages


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import IntegrityError




def jobView(request):
    
    # if request.method=="POST":
    #     email = request.POST["email"]
    #     new_signup = Signup()
    #     new_signup.email = email
    #     new_signup.save()

    # category_count = get_category_count()
    most_recent_post = JobPost.objects.order_by("-post_date")[0:3]
    
    featured_post = JobPost.objects.all()
    
    paginator = Paginator(featured_post, 8)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)   
    context = {
        # "category_count":category_count,
        'queryset':paginated_queryset,
        "page_request_var":page_request_var ,
        "featured_post":featured_post,
        "most_recent_post":most_recent_post,
        
        
    }
   

    return render(request, 'jobs/jobview.html', context)



def jobDetail(request, id):
    most_recent = JobPost.objects.order_by('-timestamp')[:3]
    post = get_object_or_404(JobPost, id=id)
    
    # lets handle enernimouse user authentication error
    # if request.user.is_authenticated:
    #     PostView.objects.get_or_create(user=request.user, post=post)

    # PostView.objects.get_or_create(user=request.user, post=post)


    # commentform = CommentForm(request.POST or None)

    # if request.method == 'POST':
    #     if commentform.is_valid():
    #         commentform.instance.user = request.user
    #         commentform.instance.post = post
    #         commentform.save()
    #         return redirect(reverse("post_detail", kwargs={
    #             'id':post.pk
    #         }))
    
    context = {
        'post':post,
        'most_recent':most_recent,
        # 'commentform':commentform,
    
    }
   
    return render(request, 'jobs/jobdetail.html', context)


def listJob(request):
    title = "CREATE"
    err_msg = ''
    message = ""
    if request.user.is_authenticated:
        try:
            form = JobListForm(request.POST or None, request.FILES or None)
            jobadmin = JobAdmin(request.user)
            
            if request.method == "POST":
                if form.is_valid():
                    form.instance.jobadmin = jobadmin
                    form.save()

                    return redirect(reverse("job-detail", kwargs={
                        'id':form.instance.id
                    }))
        except IntegrityError as e :
            e = "please contact admin  to gain access to post your blog"
            err_msg = e
            print(err_msg)
            return redirect('job')
    
    message = err_msg
    form = JobListForm()
    context = {
        "title":title,
        'message':message,
        'form':form,
        }

    return render(request, 'jobs/list_job.html', context)





   # job post update

def update_joblist(request):
    title = "UPDATE"
    err_msg=''
    message = ""
    post = get_object_or_404(JobPost, id=id)

    try:
        form = JobListForm(
            request.POST or 
            None, request.FILES or None,
            instance=post
            
        )
        jobadmin = JobAdmin(request.user)
        
        if request.method == "POST":
            if form.is_valid():
                form.instance.jobadmin = jobadmin
                form.save()

                return redirect(reverse("job-detail", kwargs={
                    'id':form.instance.id
                }))
    except IntegrityError as e :
        e = "please contact admin  to gain access to post your blog"
        err_msg = e
        print(err_msg)
        return redirect('job')
    
    message = err_msg
    form = JobListForm()
    context = {
        "title":title,
        
        'message':message,
        'form':form,
        }

    
    return render(request, 'jobs/list_job.html', context)
