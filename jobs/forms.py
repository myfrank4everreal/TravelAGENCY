from django import forms
from django.db.models import fields
from django.forms import TextInput
from crispy_forms.helper import FormHelper


from .models import JobPost

from tinymce import TinyMCE


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class JobListForm(forms.ModelForm):
    more_detail = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols':30, 'rows':10}
        )
    )

    def __init__(self, *args, **kwargs):
        super(JobListForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False 

    class Meta:
        model = JobPost
        # select the field we need in the create form

        fields = [
            'job_title', 
            'job_description',
            'requirements',
            'category',
            # 'job_admin_name',
            'country',
            'locations',
            'company_name',
            'more_detail',
        ]


        

#  class="form-control" name="message" rows="5" placeholder="Leave your message"
# class CommentForm(forms.ModelForm):
#     comment = forms.CharField(widget=forms.Textarea(attrs={
#         'class':'form-control',
#         "name":"message",
#         "rows":"5",
#         "placeholder":"Leave your message"
#     }))
#     class Meta:
#         model = Comment
#         fields = ['comment']

        