from django.urls import path
from . import views


urlpatterns = [
    path('', views.jobView, name= "job"),
    path('presic-jobs/create-job/', views.createJob, name='make-job'),
    path('search-result', views.searchjob, name='job-search'),

    
    
]


