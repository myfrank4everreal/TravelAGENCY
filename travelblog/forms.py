from django import forms
from django.db.models import fields
from django.forms import TextInput
from crispy_forms.helper import FormHelper


from .models import Blog, Comment

from tinymce import TinyMCE


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class BlogForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols':30, 'rows':10}
        )
    )

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False 

    class Meta:
        model = Blog
        # select the field we need in the create form

        fields = ['title', 'description', 'detail_content', 'image', 'category', 'featuredpost']


        

#  class="form-control" name="message" rows="5" placeholder="Leave your message"
class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        "name":"message",
        "rows":"5",
        "placeholder":"Leave your message"
    }))
    class Meta:
        model = Comment
        fields = ['comment']

        