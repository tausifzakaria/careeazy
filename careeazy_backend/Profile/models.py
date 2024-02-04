from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    phone = models.CharField(max_length=14)
    blood_group = models.CharField(max_length=4,null=True,blank=True)
    dob = models.DateField(null=True,blank=True)
    profile_pic = models.ImageField(null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.ForeignKey("Address",on_delete=models.CASCADE,null=True,blank=True)

class DoctorProfile(models.Model):
    phone = models.CharField(max_length=14)
    speciality = models.CharField(max_length=14)
    dob = models.DateField(null=True,blank=True)
    profile_pic = models.ImageField(null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.ForeignKey("Address",on_delete=models.CASCADE,null=True,blank=True)


class Address(models.Model):
    city = models.CharField(max_length=255)
    landmark = models.CharField(max_length=255,null=True,blank=True)
    pincode = models.IntegerField()
    address = models.TextField()

class ClinicProfile(models.Model):
    name = models.CharField(max_length=255)
    open_time = models.TimeField()
    close_time = models.TimeField()
    open_days = models.CharField(max_length=255)
    address = models.ForeignKey("Address",on_delete=models.CASCADE,null=True,blank=True)