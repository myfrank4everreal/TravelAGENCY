from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError("the given email is already registered")
        return self.cleaned_data['email']
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2' ]
        
        widgets={
                 'first_name':forms.TextInput(attrs={"type":"text", "class":"form-control ",'name':'last_name', "placeholder":"Last name", "aria-label":"Last name"}),
                 'last_name':forms.TextInput(attrs={"type":"text", "class":"form-control ",'name':'last_name', "placeholder":"Last name", "aria-label":"Last name"}),
                 'username':forms.TextInput(attrs={"type":"text", "class":"form-control ",'name':'username', "placeholder":"Username", "aria-label":"Username"}),
                 'email':forms.TextInput(attrs={"type":"email", "class":"form-control ",'name':'email', "placeholder":"email", "aria-label":"email"}),
                 'password1':forms.TextInput(attrs={"type":"password", "class":"form-control ", 'name':'password1', "placeholder":"password", "aria-label":"password"}),
                 'password2':forms.TextInput(attrs={"type":"password", "class":"form-control ", 'name':'password2', "placeholder":" re-enter password", "aria-label":"password comfirmation"})
                 }
        
        
        
        
        
        