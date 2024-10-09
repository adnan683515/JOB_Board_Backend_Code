from django.db import models

# Create your models here.
class Place(models.Model):
    name= models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,null=True,blank=True)
    

    def __str__(self):
        return self.name
    
    
    
class Browse_cetagory(models.Model):
    name= models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return self.name
    

class organizationtype(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return self.name
    
class work_type(models.Model):
    name= models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,null=True,blank=True)
    
    
    def __str__(self):
        return self.name
    