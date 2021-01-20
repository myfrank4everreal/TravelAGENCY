from django.db.models.query import QuerySet
from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Q
from django.urls.base import reverse
from .models import Blog, Author
from .forms import CommentForm
from .models import Comment
from marketing.models import Signup
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import BlogForm


def get_author(user):
    queryset = Author.objects.filter(user=user)
    if queryset.exists():
        return queryset[0]
    return None


def search(request):
    queryset = request.Get.get('q')
    query = request.Get.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__iconatains=query) | 
            Q(detail__icontains=query)

        ).distinct()
    context = {
        "queryset":queryset
    }

    return render(request, 'travelblog/search_result.html', context)


# def get_category_count():
#     queryset = Blog.objects.values('category__title').annotate(Count("category__title"))
#     return queryset


def blogView(request):
    if request.method=="POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    # category_count = get_category_count()
    most_recent_post = Blog.objects.order_by("-post_date")[0:3]
    
    featured_post = Blog.objects.all()
    paginator = Paginator(featured_post, 4)
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
   

    return render(request, 'travelblog/blogview.html', context)



def blogDetail(request, id):
    post = get_object_or_404(Blog, id=id)
    commentform = CommentForm(request.POST or None)

    if request.method == 'POST':
        if commentform.is_valid():
            commentform.instance.user = request.user
            commentform.instance.post = post
            commentform.save()
            return redirect(reverse("post_detail", kwargs={
                'id':post.pk
            }))
    
    context = {
        'post':post,
        'commentform':commentform,
    
    }
   
    return render(request, 'travelblog/blogdetails.html', context)

def post_create(request):
    form = BlogForm(request.POST or None, request.FILES or None)

    author = get_author(request.user)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()

            return redirect(reverse("post_detail", kwargs={
                'id':form.instance.id
            }))
    context = {
        'form':form,
        }

    return render(request, 'travelblog/post_create.html', context)
    



def post_update(request, id):
    pass


def post_delete(request, id):
    pass