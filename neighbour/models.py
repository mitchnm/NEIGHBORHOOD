from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    profile_pic = models.ImageField(upload_to = 'neighbourhood/',blank=True)
    bio = models.CharField(max_length=250, null=True)
    neighbourhood = models.ForeignKey('Neighbourhood')


class Neighbourhood(models.Model):
    name = models.CharField(max_length=60)
    picture = models.ImageField(upload_to = 'neighbourhood/',blank=True)
    location = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Business(models.Model):
    business_name = models.CharField(max_length=60)
    image = models.ImageField(upload_to = 'neighbourhood/',blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    neighbourhood = models.ForeignKey('Neighbourhood')
    business_email = models.EmailField(max_length=100)


class Post(models.Model):
    image = models.ImageField(upload_to = 'neighbourhood/')
    description = models.CharField(max_length=500)
    neighbourhood = models.ForeignKey('Neighbourhood')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('Profile', null=True)
    
    def save_profile(self):
        self.save()