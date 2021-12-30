from django import forms
from django.db import models
from django.db.models import fields
from .models import Profile
from django.contrib.auth.models import User
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

DEFAULT_ATTRS = {'data-lpignore': 'true'}

class LoginForm(forms.Form):
    username = forms.CharField(label="username", label_suffix="", widget=forms.TextInput(attrs={
        'class':'input100','placeholder':'نام کاربری را وارد نمایید', 'title':''
    }))
    password = forms.CharField(label="password", label_suffix="", widget=forms.PasswordInput(attrs={
        'class':'input100','placeholder':'کلمه عبور را وارد نمایید', 'title':''}))
    


class ProfileForm(forms.ModelForm):
    # username = forms.CharField(label='نام کاربری')
    # password = forms.CharField(label='کلمه عبور', widget=forms.PasswordInput)
    bio = forms.CharField(label='درباره من', required=False)
    phone= forms.CharField(label='شماره همراه', required=False)
    gender=forms.CharField(label='جنسیت', required=False)
    nc=forms.CharField(label='کدملی', required=False, widget=forms.TextInput(attrs=DEFAULT_ATTRS))
    resume =forms.FileField(label='رزومه', required=False)
    avatar=forms.ImageField(label='عکس', required=False)
    is_author=forms.BooleanField(label='نویسنده؟', required=False)
    class Meta:
        model=User
        fields=['username','first_name', 'last_name', 'email', 'date_joined']
        labels={}
        help_texts={'username':"",}


class RegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name', 'last_name', 'email','password']
        labels={}
        help_texts={'username':"",}
    confirm_password = forms.CharField(label='تکرار گذر واژه', widget=forms.PasswordInput)
    phone= forms.CharField(label='شماره همراه', required=False)
    age= forms.CharField(label='سن', required=False)
    gender=forms.CharField(label='جنسیت', required=False)
    nc=forms.CharField(label='کدملی', required=False, widget=forms.TextInput(attrs=DEFAULT_ATTRS))
    resume =forms.FileField(label='رزومه', required=False)
    
    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )


    
    # def clean_username(self):
    #     data = self.cleaned_data["username"]
    #     if len(data) < 5:
    #         self.add_error('username', 'نام کاربری می بایست بیشتر از 5 حرف باشد')
    #     return data
    

