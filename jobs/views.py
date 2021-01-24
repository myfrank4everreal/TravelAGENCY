from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from .models import JobPost

from django.db.models.query import QuerySet
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




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