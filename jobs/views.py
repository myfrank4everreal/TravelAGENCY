from genericpath import exists
from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from .models import JobAdmin, Jobs, JobCategory, City
from .forms import JobListForm
from django.db.models.query import QuerySet
from django.db.models import Q
from django.urls.base import reverse
from django.core.checks import messages
from django.db.models import Q

from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import IntegrityError

from django.contrib.auth.decorators import login_required, permission_required









def searchjob(request):
    queryset = Jobs.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(job_title__icontains=query) |
            Q(job_description__icontains=query)
        ).distinct()
    context={
        'queryset':queryset
    }
    return render(request, 'jobs/search_result.html', context)
    
    

def createJobAdmin(user):
    jobadmin = JobAdmin.create(user=user)
    jobadmin.save()
    return jobadmin


def getJobAdmin(user):
    jobadmin = JobAdmin.objects.filter(user=user)
    
    if jobadmin.exists :
        for i in jobadmin:
            if len(i) >=1:
                return jobadmin[0]
    
    else:
        createJobAdmin(user)
        
        
    

def jobView(request):
    
    most_recent_post = Jobs.objects.order_by("-post_date")[0:8]
    
    featured_post = Jobs.objects.all()
    
    paginator = Paginator(featured_post, 8)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages) 
        
    # category view
    category_list = JobCategory.objects.all()
    city_list = City.objects.all()
    context = {
        # "category_count":category_count,
        
        'city_list' : city_list,
        'category_list' : category_list,
        'queryset':paginated_queryset,
        "page_request_var":page_request_var ,
        "featured_post":featured_post,
        "most_recent_post":most_recent_post, 
    }

    # return render(request, 'accounts/register.html', context)
    return render(request, 'jobs/jobview.html', context)

def cityjob(request, id):
    title = 'city'
    
    cityobj = get_object_or_404(City, id=id)
    cityjobs = cityobj.jobs_set.all()
    
    paginator = Paginator(cityjobs, 8)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages) 
        
    context = {
        'cityobj':cityobj,
        'queryset':paginated_queryset,
        'title':title,
        }
    return render(request, 'jobs/cityjobs.html', context)
    

def catjobs(request, id):
    title = 'category'
    catobj = get_object_or_404(JobCategory, id=id)
    cityjobs = catobj.job_set.all()
    
    paginator = Paginator(cityjobs, 8)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages) 
        
    context = {
        'queryset':paginated_queryset,
        'title':title,
        }
    return render(request, 'jobs/cityjobs.html', context)


def jobDetail(request, id):
    most_recent = Jobs.objects.order_by('-post_date')[:3]
    post = get_object_or_404(Jobs, id=id)
    
    context = {
        'post':post,
        'most_recent':most_recent,
        # 'commentform':commentform,
    
    }
   
    return render(request, 'jobs/jobdetail.html', context)

def createJob(request):
    title = "CREATE"
    err_msg = ''
    message = ""
    form = JobListForm()
    
    if request.user.is_authenticated:
        try:
            form = JobListForm(request.POST or None, request.FILES or None)
            user = request.user
                            
            jobadmin = getJobAdmin(user)
            
            
            print('this is the : {}' .format(jobadmin))
            
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
    else:
        return redirect('job')
    message = err_msg
    context = {
        'jobadmin':jobadmin,
        "title":title,
        'message':message,
        'form':form,
        }

    return render(request, 'jobs/createjob.html', context)

   # job post update

def updateJob(request, id):
    title = "UPDATE"
    err_msg=''
    message = ""
    post = get_object_or_404(Jobs, id=id)

    try:
        form = JobListForm(request.POST or None, request.FILES or None, instance=post)
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

    
    return render(request, 'jobs/createjob.html', context)
