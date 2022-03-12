"""travelsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from travelblog.views import blogView, blogDetail, search, post_delete, post_create, post_update
from jobs.views import jobView, jobDetail, updateJob, cityjob, catjobs, createJob

from accounts.views import dashbaord
from filebrowser.sites import site





urlpatterns = [
    # path('admin/filebrowser/', site.urls),
    path('admin/', admin.site.urls),
    
    
    path('tinymce/', include('tinymce.urls')),
    path('', include('travel.urls', namespace="travel")),
    
    path('search/', search, name= 'search' ),
    
    
    # for the job app
    
    path('presic-jobs/', include('jobs.urls')),
    path('presic-jobs/', jobView, name='job'),
    path('presic-jobs/city/<id>/', cityjob, name='city-job'),
    path('presic-jobs/category/<id>/', catjobs, name='category'),
    
    path('presic-jobs/<id>/', jobDetail, name='job-detail'),
    path('presic-jobs/<id>/job-list-update', updateJob, name='job-update'),
    # path('job-list-delete/<id>/', jobDetail, name='job-detail'),


    # for the  blog 
    # path('blog/', include('travelblog.urls')),
    path('blog/', blogView, name='blog'),
    path('blog/<id>/', blogDetail, name='post_detail'),
    path('create-blog/', post_create, name='post-create'),
    path('blog/<id>/update', updateJob, name='post-update'),
    path('blog/<id>/delete', post_delete, name='post-delete'),
    
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('accounts.urls')),
   
    # for the dashboard
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT )
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT )

