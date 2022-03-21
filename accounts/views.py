from tokenize import group
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect
from .forms import RegistrationForm
from jobs.models import JobCategory,Jobs, JobAdmin
from travelblog.models import Blog
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib import messages
from travelblog.models import Author

from .decorators import allowed_users, authenticated_user

# Create your views here.

def register_user(request):
    form = RegistrationForm(request.POST or None)
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print('this is the new user :', user)
            group = Group.objects.get(name='jobadmin')
            print('this is the group :', group)
            user.groups.add(group) 
            
            jobadmin = JobAdmin(user=user)
            jobadmin.save()
            print(dir(JobAdmin))

            return redirect('login')

    context = {'form':form}
    return render(request, 'accounts/register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        # Email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully loged in ')
            return redirect('dashboard')
        else:
            messages.error(request, 'user not found')    
    return render(request, 'accounts/login.html')



def logout_user(request):
    logout(request)
    return redirect('job')

@login_required(login_url='login')
@allowed_users(allowed_roles=['jobadmin'])
def dashbaord(request):
           
    try:
        admin_job = request.user.jobadmin.jobs_set.all()
    except:
        return render(request, 'accounts/newuser.html')
    author_posts = request.user.author.get_author_posts
    
    context = {'admin_job':admin_job,
               'author_posts':author_posts
               }
    return render(request, 'accounts/dashboard.html', context)



