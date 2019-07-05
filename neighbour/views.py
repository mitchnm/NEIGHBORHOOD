from django.shortcuts import render
from .models import Post, Profile, Neighbourhood, Post

# Create your views here.
def welcome(request):
    return render(request, 'index.html')