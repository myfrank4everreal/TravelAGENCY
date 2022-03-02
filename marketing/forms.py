from importlib.abc import MetaPathFinder
from django import forms
from .models import Reports




class ContactForm(forms.ModelForm):
    class Meta:
        model = Reports
        fields = ['name', 'email', 'message']
        widgets={'name':forms.TextInput(attrs={"type":"text", "name" :'name', "class":"form-control", "placeholder":"name", "aria-label":"Username"}),
                 'email':forms.TextInput(attrs={"type":"email", "name" :'email', "class":"form-control", "placeholder":"email", "aria-label":"Username"}),
                 'message':forms.Textarea(attrs={"type":"textarea", "name" :'message', "class":"form-control", "placeholder":"message", "aria-label":"with textarea"}),
                 
                 }
        