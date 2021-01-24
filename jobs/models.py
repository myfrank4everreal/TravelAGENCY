from django.db import models



from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from django.db.models.fields import TextField
from django.urls import reverse

# for tynymce

# from tinymce import HTMLField
from ckeditor.fields import RichTextField

User = get_user_model()

# class Comment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
   
#     # user = models.OneToOneField(User, on_delete=models.CASCADE)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     comment = models.TextField()
#     post = models.ForeignKey('Blog', related_name='comments', on_delete=models.CASCADE)


#     def __str__(self):
#         return self.user.username




  # to handdle the view count we a postview class
# class JobPostView(models.Model):
#     user = models.ForeignKey(User, on_delete=CASCADE)
#     post = models.ForeignKey('JobPost', on_delete=CASCADE)

#     def __str__(self):
#         return self.user.username

# now we will no longer make use of the viewcount field of the 
# Blog rather we create a proper to handle view count like we did 
# with the comment count


class JobAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='media', default='img/avata/avataars.png')

    def __str__(self):
        return self.user.username

class JobCategory(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title   


class JobPost(models.Model):
    application_link = models.CharField(max_length=300, blank=True, null=True)

    company_name = models.CharField(max_length=300, default=None)
    job_title = models.CharField(max_length=200, default=None)
    job_description = models.TextField()
    salary = models.IntegerField(default=0)
    locations = models.CharField(max_length=500, default=None)
    country = models.CharField(max_length=300, blank=True, null=True)
    counter = models.IntegerField(default=0)
    requirements = models.TextField(default=None)
    # comment_count = models.IntegerField(default=0)
    # view_count = models.IntegerField(default=0)
    post_date = models.DateTimeField(auto_now_add=True)
    
    featuredjobs = models.BooleanField(default=False)
    category = models.ManyToManyField(JobCategory)
    job_admin_name = models.ForeignKey(JobAdmin, blank=True, null=True, on_delete=models.CASCADE)
    # for the tinymce
    # content = HTMLField('Content')
    more_detail = RichTextField(blank=True, null=True)

    
    def __str__(self):
        return self.job_title

    def shotend_desc(self):
        return self.job_description[:100] + '...'



    def get_absolute_url(self):
        return reverse('job-detail', kwargs={"id":self.id})
    
    
    def get_update_url(self):
        return reverse('job-update', kwargs={"id":self.id})

    def get_delete_url(self):
        return reverse('job-delete', kwargs={"id":self.id})

# # return reverse('people.views.details', args=[str(self.id)])
# # kwargs={"id": self.id}
  


#     # this is how we get all the comment  from users
#     @property
#     def get_comments(self):
#         return self.comments.all().order_by("-timestamp")

#     # this is for the comment count
#     @property
#     def comment_count(self):
#         return Comment.object.filter(post=self).count()


# #  this is the property for the view count.
#     @property
#     def view_count(self):
#         return PostView.objects.filter(post=self).count()
    
# class Comment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
   
#     # user = models.OneToOneField(User, on_delete=models.CASCADE)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     comment = models.TextField()
#     post = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)


#     def __str__(self):
#         return self.user.username


