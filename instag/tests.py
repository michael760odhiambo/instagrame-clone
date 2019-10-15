from django.test import TestCase
import datetime as dt
from .models import Profile,Comment,Image,Like

class ProfileTestClass(TestCase):
    def setUp(self):
        self.mike = Profile(title='Asembo',photo='default.jpg',bio='he is from there',created_on='auto_now_add=True')

    def test_instance(self):
        self.assertTrue(isinstance(self.mike, Profile))

    def test_save_methods(self):
        self.mike.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)  

    def tearDown(self):
        Profile.objects.all().delete()
# Create your tests here.
