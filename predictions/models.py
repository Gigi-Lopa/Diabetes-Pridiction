from django.db import models

# Create your models here.
class usersModel(models.Model):
    username = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
class userHistory(models.Model):
    userId = models.ForeignKey(usersModel, on_delete=models.CASCADE)
    preg = models.IntegerField(max_length=100)
    glucose  =models.IntegerField(max_length=100)
    BP = models.IntegerField(max_length=100)
    insulin = models.IntegerField(max_length=100)
    BMI = models.FloatField(max_length=255)
    DPF = models.IntegerField(max_length=2)
    age = models.IntegerField(max_length=100)
    prediction = models.CharField(max_length=50)

class adminSec(models.Model):
    admin_username = models.CharField(max_length=50)
    admin_password = models.CharField(max_length=50)    
