from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect
from .forms import RegistrationForm
from jobs.models import JobCategory,Jobs, JobAdmin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.

def register_user(request):
    form = RegistrationForm(request.POST or None)
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    
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

@login_required
def dashbaord(request):
    user = request.user
    # print('this is the user dir %s '%dir(user))
    print(f" this is the first name : {user}")
    job_admin_users = JobAdmin.objects.all()
    
    for job_admin in job_admin_users:
        print(f'this is the job_admi: {job_admin}')
        if not user == job_admin:
            return redirect('job')
            
        else:
            admin_job = request.user.jobadmin.jobs_set.all()
            
    context = {'admin_job':admin_job}
    return render(request, 'accounts/dashboard.html', context)



