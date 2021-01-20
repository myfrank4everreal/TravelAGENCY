from django import forms
from django.db.models import fields
from django.forms import TextInput


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


    class Meta:
        model = Blog
        # select the field we need in the create form

        fields = ('title', 'detail', 'content', 'image',
        'category', 'featuredpost')



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

        