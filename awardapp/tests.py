from django.test import TestCase
from .models import Comment,Post,Profile
from django.core.files.uploadedfile import SimpleUploadedFile


class ContentRatingTestClass(TestCase):
    # set up method to test for comments and instatiating the image object

    def setUp(self):
        self.test_rates = ContentRating(rating= 'The good life',user= 'shaw',project='jpg')
        self.test_rates.save()

    # Testing instance 
     
    def test_instance(self):
        self.assertTrue(isinstance(self.test_rates, ContentRating))
    
    # Testing the saving method 

    def test_save_method(self):
        rates = ContentRating.objects.all()
        self.assertTrue(len(rates)>0)
    #Tear down method    

    def tearDown(self):
        Comment.objects.all().delete()
    
     # Testing delete method 
    def test_delete_comments(self):
        self.test_comments.delete()
        self.assertAlmostEqual(len(Comments.objects.all()), 0)


class ProfileTestClass(TestCase):
    # set up method to test instantiation is correct

    def setUp(self):
        self.test_profile = Profile(bio='Master willen',profile_photo='imagejpg')
        self.test_profile.save()
    
    # Testing instance 
    def test_instance(self):
        self.assertTrue(isinstance(self.test_profile, Profile))
    
    # Testing the save method
    def test_save_method(self):
        profile = Profile.objects.all()
        self.assertTrue(len(profile)>0)
    
    # Tear dowm method 
    def tearDown(self):
        Profile.objects.all().delete()
    
    # Testing delete method 
    def test_delete_profile(self):
        self.test_profile.delete()
        self.assertEqual(len(Profile.objects.all()), 0) 
    

  


    

    