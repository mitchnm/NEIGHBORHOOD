from django.shortcuts import render, redirect
from .models import Post, Profile, Neighbourhood, Business
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, PostForm, NeighbourhoodForm, BusinessForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    neighbourhood = Neighbourhood.objects.all()
    return render(request, 'index.html', {"neighbourhood": neighbourhood})


@login_required(login_url='/accounts/login/')
def profile(request, id):
    post = Post.objects.filter(user_id=id)
    neighbourhood = Neighbourhood.objects.get(id=id)
    current_user = request.user
    user = User.objects.get(id=id)
    try:
        profile = Profile.objects.get(user=id)
    except ObjectDoesNotExist:
        return render(request, 'profile.html')
    return render(request, 'profile.html', {"post": post, "user": user, "profile": profile})


@login_required(login_url='/accounts/login/')
def update_profile(request, id):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.username = current_user
            profile.user_id = current_user.id
            profile.save()
        return render(request, 'profile.html')

    else:
        form = ProfileForm()
    return render(request, 'update_profile.html', {"form": form, "user": current_user})


@login_required(login_url='/accounts/login/')
def new_post(request, id):
    current_user = request.user
    neighbourhood = Neighbourhood.objects.get(id=id)
    if request.method == 'POST':
        print('noo')
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.user.id = current_user.id
            post.neighbourhood = neighbourhood
            post.neighbourhood.id = neighbourhood.id
            post.save()
        return redirect('welcome')

    else:
        form = PostForm()
        print('xyz')
    return render(request, 'post.html', {"form": form, 'user': current_user, "neighbourhood": neighbourhood})


@login_required(login_url='/accounts/login/')
def search_results(request):

    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles = Neighbourhood.objects.filter(
            name__icontains=search_term)
        neighbourhood = Neighbourhood.objects.all()
        message = f"{search_term}"
        return render(request, 'search.html', {"message": message, "neighbourhood1": searched_profiles, "neighbourhood": neighbourhood})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})


@login_required(login_url='/accounts/login/')
def new_neighbourhood(request, id):
    current_user = request.user
    if request.method == 'POST':
        print('noo')
        form = NeighbourhoodForm(request.POST, request.FILES)
        if form.is_valid():
            neighbourhood = form.save(commit=False)
            neighbourhood.user = current_user
            neighbourhood.save()
        return redirect('welcome')

    else:
        form = NeighbourhoodForm()
        print('xyz')
    return render(request, 'add_neighbourhood.html', {"form": form, 'user': current_user})


@login_required(login_url='/accounts/login/')
def add_business(request, id):
    current_user = request.user
    neighbourhood = Neighbourhood.objects.get(id=id)
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.username = current_user
            business.user_id = current_user.id
            business.neighbourhood = neighbourhood
            business.neighbourhood.id = neighbourhood.id
            business.save()
        return redirect('welcome')

    else:
        form = BusinessForm()
    return render(request, 'business.html', {"form": form, "user": current_user, "neighbourhood": neighbourhood})


@login_required(login_url='/accounts/login')
def join(request, id):
    neighbourhood = Neighbourhood.objects.get(id=id)
    post = Post.objects.get(id=id)
    business = Business.objects.get(neighbourhood_id=id)
    return render(request, 'neighbourhood.html', {"neighbourhood": neighbourhood,"post":post,"business":business})
