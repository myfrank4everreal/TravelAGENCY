from django.contrib import admin
from .models import JobPost, JobCategory, JobAdmin






admin.site.register(JobPost)
admin.site.register(JobCategory)
admin.site.register(JobAdmin)
