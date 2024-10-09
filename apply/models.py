from django.db import models
from django.contrib.auth.models import User
from job.models import JOB
from place.models import Browse_cetagory
# Create your models here.


apply_status = [
    ('Pendding','Pendding'),
    
    ('Accepted','Accepted')
]


class Apply(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='apply')
    job = models.ForeignKey(JOB,on_delete=models.CASCADE)
    
    
    
    
    phone_number = models.CharField(max_length=13,null=True,blank=True)
    image = models.CharField(max_length=100,null=True,blank=True)
    status = models.CharField(choices=apply_status,null=True,blank=True,max_length=100)
    
    
    # Experience
    title= models.CharField(max_length=100,null=True,blank=True)
    company = models.CharField(max_length=100,null=True,blank=True)
    office_location = models.CharField(max_length=100,null=True,blank=True)
    






    
    education = models.CharField(max_length=200)
    facebookLink = models.CharField(max_length=200)
    resume =  models.CharField(max_length=100,null=True,blank=True)
    
    

    