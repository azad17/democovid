from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class District(models.Model):
    district = models.CharField(max_length=20)
    def __str__(self):
        return self.district

class Center(models.Model):
    district = models.ForeignKey(District,on_delete=models.CASCADE)
    center = models.CharField(max_length=30)
    def __str__(self):
        return self.center

class Authority(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    designation = models.CharField(max_length=50)
    history = models.TextField(max_length=1000)
    pic = models.ImageField(upload_to='pics')
    def __str__(self):
        return self.name

class Booking(models.Model):
    VACCINES = (
        ('Covaccine','Covaccine'),
        ('Covishield','Covishield'),
        ('Sputnic ','Sputnic'),
    )
    TIMES = (
        ('9am','9am'),
        ('2pm','2pm'),
        ('4pm','4pm'),
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    vaccine = models.CharField(max_length=10,choices=VACCINES)
    district = models.ForeignKey(District,on_delete=models.CASCADE)
    center = models.ForeignKey(Center ,on_delete=models.CASCADE)
    time = models.CharField(max_length=10,choices=TIMES)
    aadhar = models.CharField(max_length=12)
    mobile = models.CharField(max_length=11)
    def __str__(self):
        return self.name

