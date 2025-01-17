from django.db import models
from django.contrib.auth.models import User
# Create your models h
class Feature(models.Model):
    phone = models.PositiveIntegerField(default=000000000)  
    bod = models.CharField(max_length=100, default='1st Jan, 2000')
    city = models.CharField(max_length=100, default='Lucknow')
    age = models.PositiveIntegerField(default=0)  
    degree = models.CharField(max_length=100, default='B.tech')
    email = models.EmailField(max_length=100, default='adsri@gmail.com') 
############################################################################################################
#useful for quiz app

class question(models.Model):
    question = models.CharField(max_length=500)
    options = models.JSONField(default=list)  # Store all options as a list of strings
    answer = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default='General') 
     
class QuizResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User model
    category = models.CharField(max_length=255)  # Title of the quiz
    score = models.IntegerField()
    total_score = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)    