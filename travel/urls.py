
from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('About-us', views.aboutUs, name='aboutus'),
    path('Dashboard', views.dashBoard, name='dashboard'),
    
    path('travel-guide', views.travelInfo, name='travel'),
    path('visa-processing', views.visaInfo, name='visa'),
    # path('find-a-job', views.jobInfo, name='job'),
]
