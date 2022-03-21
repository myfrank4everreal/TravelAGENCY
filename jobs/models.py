from email.policy import default
from django.db import models



from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from django.db.models.fields import TextField
from django.urls import reverse
from django_countries.fields import CountryField

# for tynymce

# from tinymce import HTMLField
# from ckeditor.fields import RichTextField

User = get_user_model()



class JobAdmin(models.Model):
    
    # i change the database type from one_to_one field to ForeignKey
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='media', default='img/avata/avataars.png')

    def __str__(self):
        return self.user.username
    

class JobCategory(models.Model):
    title = models.CharField(max_length=50)
    cat_image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title   
    
    def get_category_url(self):
        return reverse('job-cats', kwargs={"id": self.id})

   
class CareerLevel(models.Model):
    title = models.CharField(max_length=600)
    
    def __str__(self):
        return self.title
    
    def get_careerlevel_url(self):
        return reverse('employment-type', kwargs={"id":self.id})
    
class EmploymentType(models.Model):
    title = models.CharField(max_length=600)

    def __str__(self):
        return self.title
    
    def get_employment_type_url(self):
        return reverse('employment-type', kwargs={"id":self.id})

class EducationalLevel(models.Model):
    title = models.CharField(max_length=400)
    
    def __str__(self):
        return self.title

class MonthlySalary(models.Model):
    amount = models.CharField(max_length=300)
    
    def __str__(self):
        return self.amount
    
class City(models.Model):
    name = models.CharField(max_length=300)
    city_image = models.ImageField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    
    def get_city_url(self):
        return reverse("city-job", kwargs={"id": self.id})
    
    

class Jobs(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    application_link = models.CharField(max_length = 200, blank=True, null=True)
    company_name = models.CharField(max_length=300, default=None)
    company_logo = models.ImageField(blank=True, null=True)
    hide_company_name = models.BooleanField()
    job_title = models.CharField(max_length=200, default=None)
    job_description = models.TextField()
    gender = models.BooleanField(choices=((None, "Any"), (True, "male"), (False, "female")), blank= True, null=True)
    
    location = models.CharField(max_length=50, blank=True, null=True)
    nationality = CountryField(multiple=True, blank=True, blank_label='optional')
    career_level = models.ManyToManyField(CareerLevel)
    employment_type = models.ForeignKey(EmploymentType, on_delete=models.CASCADE)
    remote = models.BooleanField(default=False)
    years_of_experience = models.IntegerField(default=1)
    educational_level = models.ManyToManyField(EducationalLevel)
    skill_set1 = models.CharField(max_length=300)
    skill_set2 = models.CharField(max_length=300, blank = True, null=True)
    skill_set3 = models.CharField(max_length=300, blank=True, null=True)
    cv_required = models.BooleanField(default=False)
    post_date = models.DateTimeField(auto_now_add=True)
    monthly_salary = models.ManyToManyField(MonthlySalary)
    featuredjobs = models.BooleanField(default=False)
    category = models.ManyToManyField(JobCategory)
    job_admin= models.ForeignKey(JobAdmin, blank=True, null=True, default=None, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    
    # for the tinymce
    # content = HTMLField('Content')
    # more_detail = RichTextField(blank=True, null=True)
    
    def __str__(self):
        return self.job_title
    
    def get_gender(self):
        return self.Jobs.gender

    def shotend_desc(self):
        return self.job_description[:100] + '...'



    def get_absolute_url(self):
        return reverse('job-detail', kwargs={"id":self.id})
    
    
    def get_update_url(self):
        return reverse('job-update', kwargs={"id":self.id})

    def get_delete_url(self):
        return reverse('job-delete', kwargs={"id":self.id})


    