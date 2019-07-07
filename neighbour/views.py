from django.shortcuts import render
from .models import Post, Profile, Neighbourhood,Business
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    return render(request, 'index.html')

@login_required(login_url='/accounts/login/')
def profile(request,id):
  post = Post.objects.filter(user_id=id)
  current_user = request.user
  user = User.objects.get(id=id)
  try:
    profile = profile.objects.get(user=id)
  except ObjectDoesNotExist:
    return render(request, 'profile.html')
  return render(request, 'profile.html', {"post":post, "user":user, "profile":profile})
