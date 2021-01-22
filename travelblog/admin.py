from django.contrib import admin

# Register your models here.
from .models import Blog, Category, Author, Comment, PostView





admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(PostView)



