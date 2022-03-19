

from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogView, name = 'blog' ),
    path('create-blog/', views.post_create, name='post-create'),
    path('detail', views.blogDetail, name = 'details' ),
    
]


