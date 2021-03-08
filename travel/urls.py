
from django.urls import path
from . import views


app_name = 'travel'

urlpatterns = [

    path('', views.home, name='home'),
    path('About-us', views.aboutUs, name='aboutus'),
    path('dashboard/', views.dashBoard, name='dashboard'),
    
    path('travel-guide', views.travelInfo, name='travel'),
    path('visa-processing', views.visaInfo, name='visa'),
    path('toure-guide', views.toureguiedView, name='toure-guide'),
    path('cargo', views.cargoView, name='cargo'),
    # path('find-a-job', views.jobInfo, name='job'),
]
