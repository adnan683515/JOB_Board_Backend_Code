from django.db import models
from place.models import Place,organizationtype,Browse_cetagory,work_type

# Create your models here.
emp_status = [
    ('Part Time','Part Time'),
    ('Full Time','Full Time'),
    ('Internship','Internship')
]

gen = [
    ('Male','Male'),
    ('Female','Female'),
    ('Male/Female','Male/Female'),
    ('Others','Others')
]

class Company(models.Model):
    company_name =  models.CharField(max_length=100,null=True,blank=True)
    slug = models.SlugField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return self.company_name
    

class JOB(models.Model):
    
    job_title = models.CharField(max_length=100)
    logo = models.CharField(max_length=100,null=True,blank=True)
    
    Company = models.ForeignKey(Company,on_delete=models.CASCADE,null=True,blank=True)
    
    salary = models.CharField(max_length=100,null=True,blank=True)
    age_limit = models.CharField(max_length=40)
    work_station = models.CharField(max_length=100)
    employment_status = models.CharField(max_length=100,choices=emp_status)
    application_deadline = models.DateField()
    published =models.DateField(null=True,blank=True)
    education = models.TextField()
    experience = models.TextField(null=True,blank=True)
    address = models.CharField(max_length=200,null=True,blank=True)
    other_benefits = models.TextField()
    gender = models.CharField(max_length=30,choices=gen)
    requirments = models.TextField(null=True,blank=True)
    
    
    
    Place = models.ForeignKey(Place ,on_delete=models.CASCADE)
    organizationtype = models.ForeignKey(organizationtype, on_delete=models.CASCADE)
    Browse_cetagory = models.ForeignKey(Browse_cetagory,on_delete=models.CASCADE)
    
    office_picture = models.CharField(max_length=100,null=True,blank=True)
    
    
    def __str__(self):
        return self.job_title
    