from django.db import models


# Create your models here.

class Detail(models.Model):
    aadhar = models.CharField(max_length=12)
    img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mobile = models.CharField(max_length=10)
    gender = models.TextField(choices =(('M', 'Male'),('F','Female'),('O','Others')))
    date = models.DateField(max_length=10)
    
    
class TempDisplay(models.Model):
    aadhar = models.CharField(max_length=12)
    name = models.CharField(max_length=50)
    temp = models.CharField(max_length=12)
    time = models.TimeField()
    date = models.DateField(max_length=10)