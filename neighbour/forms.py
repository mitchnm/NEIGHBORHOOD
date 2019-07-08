from .models import Post, Profile, Neighbourhood, Business
from django import forms
from django.forms import ModelForm, Textarea, IntegerField

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = [ 'user' ]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = [ 'user', 'profile' ]

class NeighbourhoodForm(forms.ModelForm):
    class Meta:
      model = Neighbourhood
      exclude = []

class BusinessForm(forms.ModelForm):
    class Meta:
      model = Business
      exclude = []