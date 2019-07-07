from .models import Post, Profile, Neighbourhood, Business
from django import forms
from django.forms import ModelForm, Textarea, IntegerField

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = [ 'name' ]


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = [ 'user', 'profile' ]

class RatingForm(forms.ModelForm):
    class Meta:
      model = Neighbourhood
      exclude = []

class RatingForm(forms.ModelForm):
    class Meta:
      model = Business
      exclude = []