from django.contrib import admin
from .models import Post, Profile, Neighbourhood, Business
# Register your models here.
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Neighbourhood)
admin.site.register(Business)