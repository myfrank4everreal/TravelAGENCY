from django import forms
from django.db.models import fields
from django.forms import TextInput
from crispy_forms.helper import FormHelper


from .models import Jobs

# from tinymce import TinyMCE


# class TinyMCEWidget(TinyMCE):
#     def use_required_attribute(self, *args):
#         return False


class JobListForm(forms.ModelForm):
    

    # def __init__(self, *args, **kwargs):
    #     super(JobListForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_show_labels = False 

    class Meta:
        model = Jobs
        # select the field we need in the create form

        fields = ['application_link', 'company_name',\
            'company_logo', 'hide_company_name', 'job_title',\
                'job_description', 'gender', 'location', 'nationality',\
                    'career_level', 'employment_type', 'remote', \
                        'years_of_experience', 'educational_level', 'skill_set1', \
                            'skill_set2', 'skill_set3', 'cv_required', \
                                'category', 'city']


