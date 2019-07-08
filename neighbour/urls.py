from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.welcome,name='welcome'),
  url(r'^profile/(\d+)',views.profile,name='profile'),
  url(r'^update_profile/(\d+)',views.update_profile,name='update_profile'),
  url(r'^post/(\d+)',views.new_post,name='post'),
  url(r'^search/', views.search_results, name='search_results'),
  url(r'^add_neighbourhood/(\d+)', views.new_neighbourhood, name='neighbourhood'),
  url(r'^business/(\d+)', views.add_business, name='business'),
  url(r'^neighbourhood/(\d+)', views.join, name='join'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)