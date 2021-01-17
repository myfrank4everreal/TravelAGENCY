

from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogView, name = 'blog' ),
    path('detail', views.blogDetail, name = 'details' ),
]


