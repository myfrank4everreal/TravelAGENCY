from django.db import models
from ckeditor.fields import RichTextField

class DService(models.Model):
    service_title = models.CharField(max_length=300)
    short_description = models.TextField(blank=True, null=True)
    service_description = RichTextField(blank=True, null=True)
    featured_services = models.BooleanField(default=False)
    service_image = models.ImageField(default=None, blank=True, null=True)
    
    def __str__(self):
        return self.service_title
