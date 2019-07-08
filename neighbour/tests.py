from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Post, Neighbourhood, Business

# Create your tests here.
class PostTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=2,username='a')
        self.newpost = Post(image='media/insta/Fashion.jpg',description='Fashion',id =1,id=3,profile=self.user)
        
    def test_instance(self):
        self.assertTrue(isinstance(self.newpost,Post))

    def test_save_image(self):
        self.newpost.save()
        post = Post.objects.all()
        self.assertTrue(len(post)>0)

class ProfileTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id =1,username='a')
        self.new_profile = Profile(name=self.user, profile_pic='media/instagram/photo.jpg',bio='I am awesome',id=2)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))

    def test_save_image(self):
        self.new_profile.save()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)>0)

class NeighbourhoodtTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id =1,username='a')
        self.newpost = Post(image='media/neighbourhood/Fashion.jpg',description='Fashion',id =1,id=3,profile=self.user)
        self.new_neighbourhood = Neighbourhood(name='boom',picture='media/neighbourhood/Fashion.jpg')
   
    def test_instance(self):
        self.assertTrue(isinstance(self.new_neighbourhood,Neighbourhood))

class BusinessTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id =1,username='a')
        self.newpost = Post(image='media/neighbourhood/Fashion.jpg',description='Fashion',id =1,id=3,profile=self.user)
        self.new_business = Business(image='media/neighbourhood/Fashion.jpg', )
   
    def test_instance(self):
        self.assertTrue(isinstance(self.new_rating,Comment))
