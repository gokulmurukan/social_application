from django import forms
from django.contrib.auth.models import User
from api.models import UserProfile,Posts,Comments
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password1","password2"]
        
        
class LogInForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class PostForm(forms.ModelForm):
    class Meta:
        model=Posts
        fields=["title","description","image"]
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.TextInput(attrs={"class":"form-control"}),
            # "image":forms.ImageField(attrs={})
        }

class UserProfileForm(forms.ModelForm):
     class Meta:
        model=UserProfile
        fields=["profile_pic","dob","place","bio","time_line_pic"]
        widgets = {'dob':forms.DateInput(attrs={"type": "date"})}