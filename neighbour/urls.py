from django.conf import settings
from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.welcome,name='welcome'),
  url(r'^profile/(\d+)',views.profile,name='profile'),
  url(r'^update_profile/(\d+)',views.update_profile,name='update_profile'),
  url(r'^project/(\d+)',views.new_post,name='post'),
  url(r'^search/', views.search_results, name='search_results'),
  url(r'^neighbourhood/(\d+)', views.new_neighbourhood, name='neighbourhood'),
]